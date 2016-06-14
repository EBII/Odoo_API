# -*- coding: utf-8 -*-

from openerp import models, api, fields, _
from datetime import datetime

class ApiViewer(models.Model):
    _name = 'apihelper.apihelper'

    @api.model
    def default_get(self, fields):
         res = self.read('apihelper.apirucher')
         import pdb
         pdb.set_trace()
         return res

    # @api.model
    # @api.returns('self')
    # def search(self):
    #     import pdb
    #     pdb.set_trace()
    #     self.lesRuches = self.read('apihelper.apirucher')
    #     return self


class ApiTerrain(models.Model):
    _name = 'apihelper.apiterrain'
    _rec_name = 'emplacement'

    # https://www.odoo.com/documentation/8.0/reference/orm.html#fields
    emplacement  = fields.Char('Emplacement')
    ressource    = fields.Many2many('apihelper.apiressource') #,'terrain_ressource','apiTerrain','apiRessource','Ressource'
    proprietaire = fields.Many2one('res.partner',u'Propriétaire')
    apiculteur   = fields.Many2one('res.partner','Apiculteur') #plusieurs apiculteur/ terrain
    actif        = fields.Boolean('actif')



class ApiTraitement(models.Model):
    _name = 'apihelper.apitraitement'
    _rec_name = 'intitule'

    #liste des traitements réaliser sur le rucher par agriculteur ou par l'apiculteur
    intitule = fields.Char('traitement')
    rucher  = fields.Many2one('apihelper.apirucher', 'Terrain')
    personne = fields.Many2one  ('res.partner', 'Qui applique')
    date     = fields.Datetime()
    type     = fields.Selection ([('terrain','agricole'),('apiculteur','sanitaire')])

class ApiRessource(models.Model):
    #type de floraisons possible
    _name = 'apihelper.apiressource'
    _rec_name = 'denomination'

    denomination = fields.Char('fleur')
    floraison    = fields.One2many('apihelper.apifloraison','floraison')
    position     = fields.Integer()  # champ compute fleuri après et avant une autre ressource

    #creer la fonction qui agrege le name
class ApiFloraison(models.Model):
    _name = 'apihelper.apifloraison'
    _rec_name = 'display_name'

    floraison     = fields.Many2one('apihelper.apiressource','Floraison')
    periode_start = fields.Date('debut floraison')
    periode_stop  = fields.Date('fin floraison')
    annee         = fields.Integer() #ne mettre que l'année
    display_name  = fields.Char(compute='_display_name') #champs compute pour affichage du nom

    @api.depends('display_name')
    def _display_name(self):
     for rec in self:
         rec.display_name = rec.floraison + str(rec.annee)

class ApiRucher(models.Model):
    #Rucher installe
    _name = 'apihelper.apirucher'

    name        = fields.Char ('Nom du rucher')
    terrain     =fields.Many2one('apihelper.apiterrain','Emplacement')
    nombre      = fields.Integer('Nombre de Ruche')
    traitement   = fields.One2many('apihelper.apitraitement', 'rucher')

# creation d'un rucher sur les valeurs du self
    @api.multi
    def duplicate(self):
        self.ensure_one()
        #take data from recordset and complete name
        vals = { 'name' : self.name + ' (duplicate)','terrain' :self.terrain.id, 'nombre' : self.nombre }
        #create new one with data and retreive Id of
        id_rucher = super(ApiRucher,self).create(vals)
        return  {   'type': 'ir.actions.act_window',
                    'res_model': 'apihelper.apirucher',
                    'name' : 'Rucher '+str(self.name)+u' Dupliqué',
                    'view_mode': 'tree',
                    'target': 'current',
                    'context': {'read': True}
        }

    @api.multi
    def new_treatment(self):
        self.ensure_one()
        vals = { 'intitule' : 'Varoa','rucher' :self.id, 'personne' : self.env.user.id, 'date' : datetime.now(),'type':'apiculteur' }
        traitement = self.env['apihelper.apitraitement']
        id_treatment = traitement.create(vals)
        #return self.env['apihelper.apitraitement'].search(id_treatment)
        return  {   'type': 'ir.actions.act_window',
                    'res_model': 'apihelper.apitraitement',
                    'name' : u'Traitement anti varoa ajouté au Rucher '+str(self.name),
                    'view_mode': 'tree',
                    'view_type': 'apicole',
                    'target': 'current',
                    'context': {'read': True}
        }

        # return {'type': 'ir.ui.view',
        #         'res_model': 'apihelper.apitraitement',
        #         'name' : 'Traitementement ajouté',
        #         #ressource associé à l id xml de l'action
        #         #'res_id':self.env.ref('popit_aggregator.action_view_aggregator').id,
        #         'view_mode': 'tree',
        #         'target': 'current',
        #         'domain': [('apihelper_apitraitement.id','=',id_treatment)]
        #         #'context': {'read': True}
        #         }

