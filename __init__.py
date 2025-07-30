from controllers.login_logout.auth_controller import auth_bp
from controllers.dashboard_controller import dashboard_bp
from controllers.cliente.cliente_routes_controller import cliente_bp
from controllers.master.master_controller import master_bp


from controllers.cliente.financeiro_routes_controller import financeiro_bp
from controllers.cliente.vendas_routes_controller import vendas_bp
from controllers.cliente.imposto_routes_controller import imposto_bp
from controllers.cliente.funcionarios_routes_controller import funcionarios_bp
from controllers.cliente.configuracoes_routes_controller import configuracoes_bp
from controllers.landing_page_controller import landing_page_bp


def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(cliente_bp)
    app.register_blueprint(master_bp)

    app.register_blueprint(financeiro_bp)
    app.register_blueprint(vendas_bp)
    app.register_blueprint(imposto_bp)
    app.register_blueprint(funcionarios_bp)
    app.register_blueprint(configuracoes_bp)
    app.register_blueprint(landing_page_bp)

