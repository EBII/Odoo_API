# -*- coding: utf-8 -*-

from openerp import models, api, fields, _
from openerp.exceptions import Warning as UserError


class WizardApihelper(models.TransientModel):
    _name = 'wizard.apihelper'
    _description = u"wizard de realisation d'action sur les terrains pour l'Api Odoo"

    information = fields.Char('texte')
    choix_model = fields.Many2one('apihelper.apiterrain')

    @api.multi
    def get_wizard(self,*args):
        print "ET LAnce le wizard"
        #myyear = date.today().year

        for click in self:
            if not self._context.get('fromWizard'):
                return {'type': 'ir.actions.act_window',
                        'res_model': 'wizard.apihelper',
                        'name' : "Lancer des actions",
                        #ressource associé à l id xml de l'action
                        #'id':self.env.ref('api_helper.wizard_apihelper_action').id,
                        'view_mode': 'form',
                        'target': 'new',
                        }

        raise UserError("Voici le wizard qui se lance pas!")



