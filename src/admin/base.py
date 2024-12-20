from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_login import current_user
from flask import redirect, url_for

class SecureModelView(ModelView):
    
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role.name == "Admin"
    
    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for("main.index"))
        
class SecureAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return False
    
    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for("main.index"))
        
    # ასევე არ მინდა home გვერდი admin პანელის ნავბარში.
    def is_visible(self):
        return False