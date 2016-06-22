# -*- coding: utf-8 -*-

from openerp import models, api, fields, _
from openerp.exceptions import Warning as UserError


class WizardApihelper(models.TransientModel):
    _name = 'wizard.apihelper'
    _description = u"wizard de realisation d'action sur les terrains pour l'Api Odoo"

    unId        = fields.Selection([('none','none'),(1,1),(2,2),(3,3),(4,4),(5,5)],'Un id de model', default='none')
    information = fields.Char('texte')
    choix_model = fields.Selection([('apihelper.apiressource','Les Ressources'),('apihelper.apiterrain','Les Terrains')
                                   ,('apihelper.apitraitement','Les Traitements'),('apihelper.apifloraison','Les Floraisons')
                                   ,('apihelper.apirucher','Les Ruchers')], "Le modele",  required=True)
    choix_champs = fields.Selection([],'Un champs')

    @api.onchange('choix_model')
    def _onchange_models(self):
        if self.choix_model != False:
            model = self.choix_model
            liste_champs =
            raise UserError(model)



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
    @api.multi
    def wz_GetIt(self):
        for me in self:
            un_id     = me.unId
            un_model  = me.choix_model
            une_value = me.information
            if un_id != 'none':
                this_Id = int(un_id)
               # rs = self.env[un_model].browse(un_id)
               #
               # return rs

                return {'type': 'ir.actions.act_window',
                'res_model': un_model,
                'res_id' : this_Id,
                'name' : 'Read',
                'view_mode': 'form',
                'nodestroy': True,
                'target': 'curent',
                #'context': {'read': True}
                }


    @api.multi
    def wz_Write(self):
        for me in self:
            un_id     = me.unId
            un_model  = me.choix_model
            une_value = me.information
            if un_id != 'none':
                this_Id = int(un_id)
               # rs = self.env[un_model].browse(un_id)
               #
               # return rs

                return {'type': 'ir.actions.act_window',
                'res_model': un_model,
                'res_id' : this_Id,
                'name' : 'Read',
                'view_mode': 'form',
                'nodestroy': True,
                'target': 'curent',
                #'context': {'read': True}
                }


    @api.multi
    def wz_Search(self):
        for me in self:
            un_model = me.choix_model
            une_value = me.information
            raise UserError("le model : "+str(un_model) +"  le texte : "+une_value )

