# Copyright 2020 Karlsruhe Institute of Technology
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from flask import redirect
from flask import render_template
from flask import request
from flask_babel import gettext as _
from flask_login import current_user
from flask_login import login_required

import kadi.lib.constants as const
from kadi.ext.db import db
from kadi.lib.permissions.core import has_permission
from kadi.lib.permissions.utils import permission_required
from kadi.lib.resources.views import update_roles
from kadi.lib.web import flash_danger
from kadi.lib.web import flash_success
from kadi.lib.web import html_error_response
from kadi.lib.web import qparam
from kadi.lib.web import url_for
from kadi.modules.accounts.models import User
from kadi.modules.records.models import Record
from kadi.modules.templates.models import TemplateType

from .blueprint import bp
from .core import create_template
from .core import delete_template as _delete_template
from .core import update_template
from .forms import AddRolesForm
from .forms import EditExtrasTemplateForm
from .forms import EditRecordTemplateForm
from .forms import NewExtrasTemplateForm
from .forms import NewRecordTemplateForm
from .models import Template
from .schemas import TemplateSchema


@bp.get("")
@login_required
@qparam("user", multiple=True, parse=int)
def templates(qparams):
    """Template overview page.

    Allows users to search and filter for templates or create new ones.
    """
    users = []

    if qparams["user"]:
        users = User.query.filter(User.id.in_(qparams["user"]))

    return render_template(
        "templates/templates.html",
        title=_("Templates"),
        js_context={"users": [(u.id, f"@{u.identity.username}") for u in users]},
    )


@bp.route("/new/<type>", methods=["GET", "POST"])
@permission_required("create", "template", None)
@qparam("template", default=None, parse=int)
@qparam("record", default=None, parse=int)
def new_template(type, qparams):
    """Page to create a new template."""
    template_type = type

    if template_type not in TemplateType.__values__:
        return html_error_response(404)

    copied_template = None
    copied_record = None

    if request.method == "GET":
        # Copy a template's metadata.
        if qparams["template"] is not None:
            copied_template = Template.query.get_active(qparams["template"])

            if copied_template is not None and (
                copied_template.type != template_type
                or not has_permission(
                    current_user, "read", "template", copied_template.id
                )
            ):
                copied_template = None

        # Copy a record's metadata.
        if qparams["record"] is not None:
            copied_record = Record.query.get_active(qparams["record"])

            if copied_record is not None and not has_permission(
                current_user, "read", "record", copied_record.id
            ):
                copied_record = None

    if template_type == TemplateType.RECORD:
        form = NewRecordTemplateForm(template=copied_template, record=copied_record)
    elif template_type == TemplateType.EXTRAS:
        form = NewExtrasTemplateForm(template=copied_template, record=copied_record)
    else:
        return html_error_response(404)

    if request.method == "POST":
        if form.validate():
            template_data = form.template_data

            if template_data is not None:
                template = create_template(
                    type=template_type,
                    title=form.title.data,
                    identifier=form.identifier.data,
                    description=form.description.data,
                    visibility=form.visibility.data,
                    data=template_data,
                )

                if template:
                    update_roles(template, form.roles.data)
                    db.session.commit()

                    flash_success(_("Template created successfully."))
                    return redirect(url_for("templates.view_template", id=template.id))

        flash_danger(_("Error creating template."))

    return render_template(
        "templates/new_template.html",
        title=_("New template"),
        template_type=template_type,
        form=form,
        js_context={"title_field": form.title.to_dict()},
    )


@bp.route("/<int:id>/edit", methods=["GET", "POST"])
@permission_required("update", "template", "id")
@qparam("key", multiple=True)
def edit_template(id, qparams):
    """Page to edit an existing template."""
    template = Template.query.get_active_or_404(id)

    if template.type == TemplateType.RECORD:
        form = EditRecordTemplateForm(template)
    elif template.type == TemplateType.EXTRAS:
        form = EditExtrasTemplateForm(template)
    else:
        return html_error_response(404)

    if request.method == "POST":
        if form.validate():
            template_data = form.template_data

            if template_data is not None:
                if update_template(
                    template,
                    title=form.title.data,
                    identifier=form.identifier.data,
                    description=form.description.data,
                    visibility=form.visibility.data,
                    data=template_data,
                ):
                    flash_success(_("Changes saved successfully."))

                    if form.submit_quit.data:
                        return redirect(
                            url_for("templates.view_template", id=template.id)
                        )

                    return redirect(url_for("templates.edit_template", id=template.id))

        flash_danger(_("Error editing template."))

    return render_template(
        "templates/edit_template.html",
        title=_("Edit template"),
        template=template,
        form=form,
        js_context={
            "title_field": form.title.to_dict(),
            "edit_extra_keys": qparams["key"],
        },
    )


@bp.get("/<int:id>")
@permission_required("read", "template", "id")
def view_template(id):
    """Page to view a template."""
    template = Template.query.get_active_or_404(id)
    schema = TemplateSchema(only=["id", "title", "identifier"])

    return render_template(
        "templates/view_template.html",
        template=template,
        js_context={"template": schema.dump(template)},
    )


@bp.get("/<int:id>/export/<export_type>")
@permission_required("read", "template", "id")
def export_template(id, export_type):
    """Page to view the exported data of a template."""
    template = Template.query.get_active_or_404(id)
    export_types = const.EXPORT_TYPES["template"]

    if export_type not in export_types:
        return html_error_response(404)

    extras = []

    if template.type == TemplateType.RECORD:
        extras = template.data.get("extras", [])
    elif template.type == TemplateType.EXTRAS:
        extras = template.data

    return render_template(
        "templates/export_template.html",
        title=export_types[export_type]["title"],
        template=template,
        export_type=export_type,
        extras=extras,
    )


@bp.route("/<int:id>/permissions", methods=["GET", "POST"])
@permission_required("permissions", "template", "id")
def manage_permissions(id):
    """Page to manage access permissions of a template."""
    template = Template.query.get_active_or_404(id)
    form = AddRolesForm()

    if form.validate_on_submit():
        update_roles(template, form.roles.data)
        db.session.commit()

        flash_success(_("Changes saved successfully."))
        return redirect(url_for("templates.manage_permissions", id=template.id))

    return render_template(
        "templates/manage_permissions.html",
        title=_("Manage permissions"),
        template=template,
        form=form,
    )


@bp.get("/<int:template_id>/revisions/<int:revision_id>")
@permission_required("read", "template", "template_id")
def view_revision(template_id, revision_id):
    """Page to view a specific revision of a template."""
    template = Template.query.get_active_or_404(template_id)
    revision = template.revisions.filter(
        Template.revision_class.id == revision_id
    ).first_or_404()

    return render_template(
        "templates/view_revision.html",
        title=_("Revision"),
        template=template,
        revision=revision,
    )


@bp.post("/<int:id>/delete")
@permission_required("delete", "template", "id")
def delete_template(id):
    """Endpoint to mark an existing template as deleted.

    Works the same as the corresponding API endpoint.
    """
    template = Template.query.get_active_or_404(id)

    _delete_template(template)
    db.session.commit()

    flash_success(_("Template successfully moved to the trash."))
    return redirect(url_for("templates.templates"))
