from fastapi import FastAPI
from mcu_web_api.routes.mcu_routes import router as mcu_router
from mcu_web_api.routes.motor_routes import router as motor_router
from mcu_web_api.routes.io_routes import router as io_router
from mcu_web_api.routes.trigger_routes import router as trigger_router
from mcu_web_api.routes.sensor_routes import router as sensor_router
from mcu_web_api.routes.ejector_routes import router as ejector_router
from mcu_web_api.routes.unit_test_routes import router as unit_test_router
from mcu_tcp_impl.server_api import DeviceManager
import threading
from js_enhanced_logging import logger
import logging
from contextlib import asynccontextmanager

# Set the logging level for 'multipart' module to suppress debug logs
logging.getLogger('multipart').setLevel(logging.WARNING)

app = FastAPI()
device_manager = DeviceManager()


@asynccontextmanager
async def startup_and_shutdown_manager(app: FastAPI):
    logger.info("FastAPI startup event triggered, starting tcp server...")
    thread = threading.Thread(target=device_manager.start, daemon=True)
    thread.start()
    try:
        yield
    finally:
        logger.info("FastAPI shutdown event triggered, stopping tcp server...")
        device_manager.stop()

app.router.lifespan_context = startup_and_shutdown_manager
# Include routers from different modules
app.include_router(mcu_router, prefix="/mcu")
app.include_router(motor_router, prefix="/motor")
app.include_router(io_router, prefix="/io")
app.include_router(trigger_router, prefix="/trigger")
app.include_router(sensor_router, prefix="/sensor")
app.include_router(ejector_router, prefix="/ejector")
app.include_router(unit_test_router, prefix="/unit-test")
