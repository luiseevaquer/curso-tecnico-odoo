# -*- coding: utf-8 -*-

from openerp import models, fields, api

'''
This module create model of Course
'''

class Course(models.Model):
    '''
    This class create model of Course
    '''
    _name = 'openacademy.course' # model odoo name

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users', 
        ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many('openacademy.session', 
        'course_id', string="Sessions")

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]
