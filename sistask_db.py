import uuid
import model_pb2
import datetime as dt

from sqlalchemy import (
    select,
    String,
    Text,
    Boolean,
    create_engine
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    Session
)

ENGINE = create_engine('sqlite:///sis_tasks.db', echo=False)

class Base(DeclarativeBase):
    pass

class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[str] = mapped_column(String(60), primary_key=True, default=lambda: str(uuid.uuid4()))
    title: Mapped[str] = mapped_column(String(100), default="Sem título")
    description: Mapped[str] = mapped_column(Text, default="Sem descrição")
    date: Mapped[str] = mapped_column(String(10), default=dt.date.today().strftime("%d/%m/%Y"))
    responsible: Mapped[str] = mapped_column(String(100), default="Sem responsável")
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False)

    def create(
            title:str, 
            description:str, 
            responsible:str,
            date:str = dt.date.today().strftime("%d/%m/%Y")
    ) -> model_pb2.TaskID:

        with Session(ENGINE) as session:
            new_task = Task(title=title, description=description, date=date, responsible=responsible)
            session.add(new_task)
            session.commit()

            return model_pb2.TaskID(id=new_task.id)
            
    def update(t:model_pb2.Task) -> model_pb2.TaskID | None:
        with Session(ENGINE) as session:
            task = session.scalars(
                select(Task).where(Task.id == t.id)
            ).first()
            if not task:
                return None 

            task.date = t.date
            task.responsible = t.responsible
            task.title = t.title
            task.description = t.description
            task.is_completed = t.is_completed

            session.commit()
            return model_pb2.TaskID(id=task.id)

    def get_task(tid:model_pb2.TaskID) -> model_pb2.Task | None:
        with Session(ENGINE) as session:
            task = session.scalars(
                select(Task).where(Task.id == tid.id)
            ).first()
            if not task:
                return None 
            return model_pb2.Task(
                id=task.id,
                title=task.title,
                date=task.date,
                responsible = task.responsible,
                description = task.description,
                is_completed = task.is_completed
            )
        
    def get_all_tasks() -> model_pb2.TaskList:
        with Session(ENGINE) as session:
            tasks = session.scalars(select(Task)).all()
            list_tasks = model_pb2.TaskList()

            for t in tasks:
                task = model_pb2.Task(
                    id=t.id,
                    title=t.title,
                    date=t.date,
                    responsible = t.responsible,
                    description = t.description,
                    is_completed = t.is_completed
                )
                list_tasks.tasks.append(task)

            return list_tasks

                
    def delete(tid:model_pb2.TaskID) -> model_pb2.Void | None:
        with Session(ENGINE) as session:
            task = session.scalars(
                select(Task).where(Task.id == tid.id)
            ).first()
            if not task:
                return None
            session.delete(task)
            session.commit()

            return model_pb2.Void()

    def finish_task(tid:model_pb2.TaskID) -> model_pb2.TaskID | None:
        with Session(ENGINE) as session:
            task = session.scalars(
                select(Task).where(Task.id == tid.id)
            ).first()
            if not task:
                return None

            task.is_completed = True
            session.commit()

            return model_pb2.TaskID(id=task.id)


Base.metadata.create_all(bind=ENGINE)