## Copyright 2016 Raik Gruenberg

## This file is part of the LabHamster project (https://github.com/graik/labhamster). 
## LabHamster is released under the MIT open source license, which you can find
## along with this project (LICENSE) or at <https://opensource.org/licenses/MIT>.

import django.forms as forms
import labhamster.models as M
import django.contrib.messages as msg


class OrderForm(forms.ModelForm):
    """Customized form for Order add/change"""
    
    def __init__(self, *args, **kwargs):
        """
        relies on self.request which is created by RequestFormAdmin
        """
        super(OrderForm, self).__init__(*args, **kwargs)
        
        ## only execute for Add forms without existing instance
        o = kwargs.get('instance', None)
        if not o and self.request: 
            ## stopped working in django 1.9:
            ## self.initial['created_by'] = str(self.request.user.id)
            self.fields['created_by'].initial = self.request.user.id
        
        ## only affects forms adding completely new entry
        self.fields['currency'].initial = M.Currency.objects.filter(is_default=True).first()


    def clean(self):
        """
        """
        data = super(OrderForm, self).clean()

        price = data.get('price', None)
        if price and not data.get('currency', None):
            msg.warning(self.request, 'Note: currency set to default (%s)' % 
                        M.Currency.objects.filter(is_default=True).first())
        
        return data

    class Meta:
        model = M.Order
        fields = "__all__" 
