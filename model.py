# -*- coding: utf-8 -*-

from openerp import models, api, fields, _


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

    denomination = fields.Char('fleur')
    floraison    = fields.One2many('apihelper.apifloraison','floraison')
    position     = fields.Integer()  # champ compute fleuri après et avant une autre ressource

    #creer la fonction qui agrege le name
class ApiFloraison(models.Model):
    _name = 'apihelper.apifloraison'
    #_rec_name = 'display_name'
    floraison     = fields.Many2one('apihelper.apiressource','Floraison')
    periode_start = fields.Date('debut floraison')
    periode_stop  = fields.Date('fin floraison')
    annee         = fields.Integer() #ne mettre que l'année
    #display_name  = fields.Char(compute='_display_name') #champs compute pour affichage du nom

    # api.depends('name')
    # def _display_name(self):
    #     for rec in self:
    #         rec.display_name = rec.denomination + str(rec.annee)

class ApiRucher(models.Model):
    #Rucher installe
    _name = 'apihelper.apirucher'

    name    = fields.Char ('Nom du rucher')
    terrain =fields.Many2one('apihelper.apiterrain','Emplacement')
    nombre  = fields.Integer('Nombre de Ruche')
    traitement   = fields.One2many('apihelper.apitraitement', 'rucher')
