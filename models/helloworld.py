# -*- coding: utf-8 -*-

from odoo import models, fields

class HelloWorldCourses(models.Model):
    _name = 'hello.world'
    _description = 'hello.world'

    name = fields.Char( 
        required=True, 
        copy=False
    )
