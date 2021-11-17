"""
Para elaborar el ejemplo se parte del codigo encontrado en https://refactoring.guru/es/design-patterns/chain-of-responsibility
El ejercicio permite alcanzar una mayor comprensión de este patrón.
Reconocimiento de los derechos de autor para el Ingeniero Shvets autor del sitio y del código original. 
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

#Se define la clase manejadora principal, como clase abstracta.
#El método set_next permite establecer la cadena de manejadores.
class Handler(ABC): 
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass

class AbstractHandler(Handler):

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None

#Implementación de cada uno de los puntos de la cadena..
class VisitanteHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Visitante":
            return f"Hola {request}, puedes solicitar registro en el sitio web, haz clic en el siguiente enlace..."
        else:
            return super().handle(request)

class RegistradoHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Registrado":
            return f"Hola {request} puedes solicitar tu matrícula en el siguiente enlace"
        else:
            return super().handle(request)

class MatriculaHomologanteHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "MatriculaHomologante":
            return f"Hola estudiante, ¿vas a homologar?, antes de continuar tu matrícula debes realizar la homologación aquí...sino...puedes continuar"
        else:
            return super().handle(request)

class MatriculaCeroHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "MatriculaCero":
            return f"Hola estudiante, en este enlace puedes matricular tus cursos para iniciar"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:

    for etapa in ["Visitante", "Registrado", "MatriculaHomologante", "MatriculaCero"]:
        print(f"\nIberoBot: Quien es {etapa}?")
        result = handler.handle(etapa)
        if result:
            print(f"  {result}", end="\n")
        else:
            print("---------------------------------------")
            print(f"  {etapa} No se encuentra este rol en el sistema.", end="\n")


if __name__ == "__main__":
    visitante = VisitanteHandler()
    registrado = RegistradoHandler()
    matriculahomologante=MatriculaHomologanteHandler()
    matriculacero = MatriculaCeroHandler()
    

    visitante.set_next(registrado).set_next(matriculahomologante).set_next(matriculacero)

    print("Chain: Visitante > Registrado > MatriculaHomologante > MatrículaCero")
    client_code(visitante)
    print("\n")
