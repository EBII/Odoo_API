# -*- coding: utf-8 -*-

from openerp import models, api, fields, _


class ApiTerrain(models.Model):
    _name = 'apihelper.apiterrain'

    # https://www.odoo.com/documentation/8.0/reference/orm.html#fields
    emplacement = fields.Char('Emplacement')
    ressource    = fields.Many2many ('apihelper.apiressource','terrain_ressource','apiTerrain','apiRessource','Ressource')
    proprietaire= fields.Many2one('res.partner',u'Propriétaire')
    apiculteur  = fields.Many2one('res.partner','Apiculteur') #plusieurs apiculteur/ terrain
    traitement  = fields.One2many ('apihelper.apitraitement', 'terrain')
    actif       = fields.Boolean('actif')

    def view_terrain(self):
        return ApiTerrain.get_default()

class ApiTraitement(models.Model):
    _name = 'apihelper.apitraitement'

    #liste des traitements réaliser sur le rucher par agriculteur ou par l'apiculteur
    intitule = fields.Char('traitement')
    terrain  = fields.Many2one('apihelper.apiterrain', 'Terrain')
    personne = fields.Many2one  ('res.partner', 'Qui applique')
    date     = fields.Datetime()
    type     = fields.Selection ([('terrain','agricole'),('apiculteur','sanitaire')])

class ApiRessource(models.Model):
    #type de floraisons possible
    _name = 'apihelper.apiressource'

    denomination  = fields.Char('fleur')
    periode_start = fields.Date('debut floraison')
    periode_stop  = fields.Date('fin floraison')
    annee         = fields.Integer() #ne mettre que l'année
    position      =fields.Integer()  # champ compute fleuri après et avant une autre ressource

class ApiRucher(models.Model):
    #Rucher installe
    _name = 'apihelper.apirucher'

    terrain =fields.Many2one('apihelper.apiterrain','Emplacement')
    nombre = fields.Integer('Nombre de Ruche')
