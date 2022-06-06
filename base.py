class base:
    def __init__(self,model):
        self.Model = model

class MetaModel(type):
    base_model = base

class baseModel(metaclass=MetaModel):
    tablename = ""


class Model(baseModel):
    base_model = base
    tablename = "Model"
    fields = ("field_1", "field_2")

model_list = [Model, ]