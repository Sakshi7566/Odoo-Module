from odoo import fields, models, api
from odoo.exceptions import ValidationError
class PosExtend(models.Model):
    _inherit ='res.partner'

    note =fields.Char()

    @api.constrains('note')
    def note_validation(self):
        alldata = self.env['res.partner']
        for rec in self:
            count = alldata.search_count([['note','=',rec.note],['id','!=',rec.id]])
        if count>0:
            raise ValidationError("Already in Exist")
    

class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_params_res_partner(self):
        load_field = super(PosSession, self)._loader_params_res_partner()
        load_field.get('search_params').get('fields').append('note')
        return load_field
    
   