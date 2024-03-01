# About
This library creates Abstract models which will be used to reduce work across all the models of your application. You can
just import the library and inherit it in other models to make usage of its functionality.

## Usage
from django_auditable_models.models import AbstractAuditableModel

```
class MyModel(models.Model,AbstractAuditableModel):
    name = models.CharField(max_length = 150,null=True,blank=True)
    
test = MyModel()
test.name = 'TestName'
test.save()

print(test.created_on)

```

Api is still underdevelopment so it can break. 