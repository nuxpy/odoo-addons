# -*- coding: utf-8 -*-

import logging
import os

import odoo
from odoo import _
from odoo import api
from odoo import fields
from odoo import models
from odoo.tools import config

_logger = logging.getLogger(__name__)


class GitRepository(models.Model):
    _name = 'git.repository'
    _description = 'Git Repositories'
    _order = 'name'

    name = fields.Char()
    url = fields.Char(string='URL')
    branch = fields.Char(default=odoo.release.version)
    addons_path = fields.Char(string='Addons Path',
        readonly=True)

    @api.model_create_multi
    def create(self, vals_list):
        # --- Addons path in data_dir:
        data_dir_path = os.path.join(config['data_dir'], 'addons', odoo.release.version)

        for vals in vals_list:
            url = vals.get('url')
            branch = vals.get('branch')
            git_account = url.split('/')[-2]
            repository = url.split('/')[-1]

            acc_path = os.path.join(data_dir_path, git_account)
            repo_path = os.path.join(data_dir_path, acc_path, repository)

            if not os.path.exists(acc_path):
                os.mkdir(acc_path, mode=0o755)

            if not os.path.exists(repo_path):
                os.mkdir(repo_path, mode=0o755)
                os.system('git clone -b {} {} {}'.format(branch, url, repo_path))
                vals['addons_path'] = '{}'.format(repo_path)
            else:
                os.system('cd {}; git pull'.format(repo_path))

        return super(GitRepository, self).create(vals_list)

    def git_pull(self):
        self.ensure_one()
        if os.path.exists(self.addons_path):
            os.system('cd {}; git pull'.format(self.addons_path))

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'context': dict(self._context, active_ids=self.ids),
            'target': 'new',
            'params': {
                'message': _("The repository was updated successfully. \
                    You must restart the Odoo service to apply changes."),
                'type': 'success',
                'sticky': False,
                'next': {'type': 'ir.actions.act_window_close'},
            }
        }

