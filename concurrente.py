import _asyncio
import asyncio
async def  tarea(tarea, tiempo):
    print(f"iniciando {tarea}")
    await asyncio.sleep(tiempo)
    print(f"finalizando {tarea}")

async def concurrente():
    await asyncio.gather(
        tarea("descarga de archivo", 2),
        tarea("Procesamiento de datos", 3),
        tarea("Registro de log", 1)
       )

asyncio.run(concurrente())