from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import routes_auth, route_predict
from app.middleware.logging_middleware import LoggingMiddleware
from app.core.exception import register_exception_handlers


app = FastAPI(title = 'Car Price Prediction')

# link middleware
app.add_middleware(LoggingMiddleware)


#link endpoints
app.include_router(routes_auth.router, tag=['Auth'])
app.inclued_router(route_predict, tag=['Prdiction'])


#monitoring using Prometheus
Instrumentator().instrument(app).expose(app)

#add exception handler 
register_exception_handlers(app)
