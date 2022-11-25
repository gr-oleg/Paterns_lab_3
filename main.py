from typing import List, Any
from datetime import datetime
from abc import ABC, abstractmethod
from collections import defaultdict
import uuid


class PersonalInfo:
    """Represintation of employee
    ...
    Attributes
    ----------
    full_name : str
        name and surname of the developer
    address : str
        relevant address
    email : str
        e-mail for work
    phone_number : str
        phone number for work
    position : str
        current position at the company
    salary : float
        income
    rank : str
        list of projects developer working on now
    """

    def __init__(self, full_name: str, address: str, phone_number: str, email: str, position: str, rank: str,
                 salary: str):
        self.full_name = full_name,
        self.address = address,
        self.phone_number = phone_number,
        self.email = email,
        self.position = position,
        self.rank = rank
        self.salary = salary

    @property
    def first_name(self) -> str:
        return self.full_name.split()[0]

    @property
    def second_name(self) -> str:
        return self.full_name.split()[1]


class Employee(ABC):
    """Represintation of employee
        ...
    Attributes
    ----------
    full_name : str
        name and surname of the developer
    address : str
        relevant address
    email : str
        e-mail for work
    phone_number : str
        phone number for work
    position : str
        current position at the company
    salary : float
        income
    rank : str
        list of projects developer working on now
    """

    def __init__(self, full_name: str, address: str, phone_number: str, email: str, position: str, rank: str,
                 salary: str) -> None:
        """Employee initialization"""

        self.id = uuid.uuid4()

        self.personal_info = PersonalInfo(
            full_name=full_name,
            address=address,
            phone_number=phone_number,
            email=email,
            position=position,
            rank=rank,
            salary=salary
        )

        @abstractmethod
        def calculate_salary(self, assigment_manager) -> float:
            """Abstract method"""
            pass

        @abstractmethod
        def ask_sick_leave(self, ):
            """Abstract method"""
            pass


class Developer(Employee):
    """
    A class used to represent a developer
    ...
    Attributes
    ----------
    _id : int
        id of the developer
    full_name : str
        name and surname of the developer
    address : str
        relevant address
    email : str
        e-mail for work
    phone_number : str
        phone number for work
    position : str
        current position at the company
    salary : float
        income
    projects : list[Projects]
        list of projects developer working on now
    assignments : list[Assignment]:
        list of assignments
    """

    def __init__(self, id: uuid.UUID, full_name: str, address: str, phone_number: str, email: str, position: str,
                 salary: str) -> None:
        """
        Method to add a developer
        ----------
        _id : int
            id of the developer
        full_name : str
            name and surname of the developer
        address : str
            relevant address
        email : str
            e-mail for work
        phone_number : str
            phone number for work
        position : str
            current position at the company
        salary : str
            income
        assignments : list[Assignment]:
            list of assignments
        """
        self.id = id
        super().__init__(full_name=full_name, address=address, email=email, salary=salary, phone_number=phone_number,
                         position=position)
        self.assignments: List[Assignment] = []

    def __str__(self):
        """String represintation of Developer"""

        return f"Developer {self.personal_info.full_name}"

    def calculate_salary(self, assigment_manager) -> float:
        project_number = len(assigment_manager.get_project_title(self.id))
        return project_number * 1000


class Task:
    """
    Representation of task
    This class provides with association/aggregation with Project class
    ...
    Attributes
    ----------
    id : int
        id of the task
    title : str
        name of the task
    deadline : datetime
        date when project have to be done
    items : list[str]
    is_done : bool
        status of the project(completed/uncompleted)
    in_progress : bool
        status of the project
    related_project : str
        title of the relaed project
    """

    def __init__(self, id: uuid.UUID, title: str, deadline: datetime, items: list[str], is_done: bool,
                 in_progress: bool, related_project: str):
        """
        A method used to create a task
        Attributes
        ----------
        id : int
            id of the task
        title : str
            name of the task
        deadline : datetime
            date when project have to be done
        items : list[str]
        is_done : bool
            status of the project(completed/uncompleted)
        in_progress : bool
            status of the project
        related_project : str
            title of the relaed project
        comment : List[str]
            A list of comments added to describe a task
        """

        self.id = id,
        self.title = title,
        self.daedline = deadline,
        self.items = items,
        self.is_done = is_done,
        self.in_progress = in_progress,
        self.related_project = related_project
        self.comments = List[str]

        def implement_item(self, item_name: str) -> str:
            self.items.append(item_name)
            print("Item " + item_name + " was added to the item list")

        def add_comment(self, commnet: str) -> None:
            self.comments.append(commnet)
            print("New comment was added")


class Assignment:
    """
    A class used to represent an assignment
    ...
    Attributes
    ----------
    received_tasks : dict
        task to do
    is_done : bool
        Is task done or not
    description : str
        short information about the task
    status : str
        current status of the assignment
    """

    def __init__(self, received_tasks: defaultdict(list), is_done: bool, description: str, status: str) -> None:
        """
        Method to create an assignment
        ...
        Attributes
        ----------
        received_tasks : dict
            task to do
        is_done : bool
            rather
        description : str
            short information about the task
        status : str
            current status of the assignment
        recived_task : dic[task]
            A list of task of the specific assignment
        """
        self.received_tasks = received_tasks
        self.is_done = is_done
        self.description = description
        self.status = status

    def get_tasks_to_date(self, date: datetime) -> List[Task]:
        """
        Returns task before date from parameters.
        -----------
        Parameters
        Date : datetime
        -------------
        Returns : list[Project]
        """
        pass


class AssignmentManager:
    """Link epmloyee with project
           ...
        Atributes
        ---------
        None
    """

    def __init__(self) -> None:
        self.employee_projects = defaultdict(list)
        self.project_employees = defaultdict(list)

    def link(self, employee_id: 'uuid.UUID', project_title: str) -> str:
        """Link employee and project
                Params
               --------
            employee_id : uuid.UUID
                id of the empoyee you want to link with specific project
            project_title : str
                title of the project you want connect employee to
        """
        if employee_id not in self.employee_projects:
            self.employee_projects[employee_id].append(project_title)
            self.project_employees[project_title].append(employee_id)
            return str(self.employee_projects[employee_id])
        else:
            raise ValueError(f"Provided employee is already signed to that project")

    def unlink(self, employee_id: 'uuid.UUID', project_title: str) -> str:
        """Unlink employee and project
                Params
               --------
            employee_id : uuid.UUID
                id of the empoyee you want to link with specific project
            project_title : str
                title of the project you want unlink employee from
        """
        if employee_id in self.employee_projects:
            self.employee_projects.pop(employee_id)
            self.project_employees.pop(project_title)
            return self.employee_projects[employee_id]
        else:
            raise ValueError(f"Provided employee is not signed to that project")

    def get_project_title(self, employee_id: int) -> List[str]:
        """get title of the current project """
        return self.employee_projects[employee_id]


class Project(ABC):
    """
    A class used to represent a project
    ...
    Attributes
    ----------
    title : str
        name of the project
    start_date : datetime
        date when project have to start
    task_list : list[dict]
        list of tasks need to be completed
    developers : list[Developer]
        list of the developer working on this project
    limit : int
        limit of the developers can be working on this project at once
    """

    def __init__(self, id: uuid.UUID, title: str, start_date: datetime, task_list: list[int], limit: int) -> None:
        """
        A method used to create a project
        ...
        Attributes
        ----------
        id : uuid.UUID
            id of the project
        title : str
            name of the project
        start_date : datetime
            date when project have to start
        task_list : list[int]
            list of tasks need to be completed
        developers : list[Developer]
            list of the developer working on this project
        limit : int
            limit of the developers can be working on this project at once
        """
        self.title = title
        self.start_date = start_date
        self.task_list = task_list
        self.limit = limit

    @abstractmethod
    def add_employee(self, employee: Employee, manager: AssignmentManager) -> None:
        """
        Method used to add a employee to project
        -----------
        Parameters
        employee: Employee
        manager : AssignmentManager
        -------------
        Returns : None
        """

        pass

    @abstractmethod
    def remove_employee(self, employee: Employee, manager: AssignmentManager) -> None:
        """
        Method used to remove a developer to project
        -----------
        Parameters
        employee: Employee
            employee to remove
        manager: AssignmentManger
            manager to remove the employee
        -------------
        Returns : None
        """
        pass


class Mobile(Project):
    """
        A class used to represent a mobile project
        ...
        Attributes
        ----------
        All attributes of Project class
    """

    def __init__(self, id: uuid.UUID, title: str, start_date: datetime, task_list: list[int], limit: int,
                 mobile_framework: str):
        super().__init__(id=id, title=title, start_date=start_date, task_list=task_list, limit=limit)
        self.mobile_framework = mobile_framework

    def add_employee(self, employee: Employee, manager: AssignmentManager) -> None:
        """
        Method used to add a employee to mobile project
        -----------
        Parameters
        employee: Employee
        manager : AssignmentManager
        -------------
        Returns : None
        """

        manager.link(employee_id=employee.id, project_title=self.title)

    def remove_employee(self, employee: Employee, manager: AssignmentManager) -> None:
        """
        Method used to remove a developer from mobile project
        -----------
        Parameters
        employee: Employee
        -------------
        Returns : None
        """
        manager.unlink(employee_id=employee.id, project_title=self.title)


class Web(Project):
    """
        A class used to represent a  web project
        ...
        Attributes
        ----------
        All attributes of Project class
    """

    def __init__(self, id: uuid.UUID, title: str, start_date: datetime, task_list: list[int], limit: int,
                 web_framework: str):
        super().__init__(id=id, title=title, start_date=start_date, task_list=task_list, limit=limit)
        self.web_framework = web_framework

    def add_employee(self, employee: Employee, manager: AssignmentManager) -> None:
        """
        Method used to add a employee to web project
        -----------
        Parameters
        employee: Employee
        manager : AssignmentManager
        -------------
        Returns : None
        """

        manager.link(employee_id=employee.id, project_title=self.title)

    def remove_employee(self, employee: Employee, manager: AssignmentManager) -> None:
        """
        Method used to remove a developer from web project
        -----------
        Parameters
        employee: Employee
        -------------
        Returns : None
        """
        manager.unlink(employee_id=employee.id, project_title=self.title)


class Embedded(Project):
    """
        A class used to represent a embedded project
        ...
        Attributes
        ----------
        All attributes of Project class
    """

    def __init__(self, id: uuid.UUID, title: str, start_date: datetime, task_list: list[int], limit: int,
                 embedded_framwork: str):
        super().__init__(id=id, title=title, start_date=start_date, task_list=task_list, limit=limit)
        self.embedded_framework = embedded_framwork

    def add_employee(self, employee: Employee, manager: AssignmentManager) -> None:
        """
        Method used to add a employee to embedded project
        -----------
        Parameters
        employee: Employee
        manager : AssignmentManager
        -------------
        Returns : None
        """

        manager.link(employee_id=employee.id, project_title=self.title)

    def remove_employee(self, employee: Employee, manager: AssignmentManager) -> None:
        """
        Method used to remove a developer from embedded project
        -----------
        Parameters
        employee: Employee
        -------------
        Returns : None
        """
        manager.unlink(employee_id=employee.id, project_title=self.title)


class QAEngineer:
    """
    A class used to represent a QAEngineer
    ...
    Attributes
    ----------
    id : int
        id of QAEngineer
    name : str
        name of the QAEngineer
    address : str
        relevant address of the QAEngineer
    phone_number : str
        phone number of the QAEngineer (work only)
    email : str
        email of the QAEngineer (work only)
    salary : float
        income
    rank : str
        current position in the company
    position : str
        current position in the company
    """

    def __init__(self, id: int, name: str, address: str, phone_number: str, email: str, salary: float, rank: str,
                 position: str) -> None:
        """
        A method used to add a QAEngineer
        ...
        Attributes
        ----------
        id : int
            id of QAEngineer
        name : str
            name of the QAEngineer
        address : str
            relevant address of the QAEngineer
        phone_number : str
            phone number of the QAEngineer (work only)
        email : str
            email of the QAEngineer (work only)
        salary : float
            income
        rank : str
            current position in the company
        position : str
            current position in the company
        """
        self.id = id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.salary = salary
        self.rank = rank
        self.position = position

    def test_feature(self, *args) -> None:
        """
        Method used to test a feature
        -----------
        Parameters
        *args : any
            depends on feature you are testing
        -------------
        Returns : None
        """
        return


class ProjectManager:
    """
    A class used to represent a QAEngineer
    ...
    Attributes
    ----------
    id : int
        id of ProjectManager
    name : str
        name of the ProjectManager
    address : str
        relevant address of the ProjectManager
    phone_number : str
        phone number of the ProjectManager (work only)
    email : str
        email of the ProjectManager (work only)
    salary : float
        income
    project : Project
        current project , ProjectManager working on
    """

    def __init__(self, id: int, name: str, address: str, phone_number: str, email: str, salary: float,
                 project: Project) -> None:
        """
        A method used to add a QAEngineer
        ...
        Attributes
        ----------
        id : int
            id of ProjectManager
        name : str
            name of the ProjectManager
        address : str
            relevant address of the ProjectManager
        phone_number : str
            phone number of the ProjectManager (work only)
        email : str
            email of the ProjectManager (work only)
        salary : float
            income
        project : Project
            current project , ProjectManager working on
        """
        self.id = id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.salary = salary
        self.project = project

    def discuss_progress(developer: Developer):
        """
        Method used to discuss progress of the current task
        with one of the developers in the project
        -----------
        Parameters
        developer : Developer
            The developer you want to have discussion with
        -------------
        Returns : None
        """
        pass

    def employee_request(self, project: Project, employee: Employee, assignment_managager: AssignmentManager):
        """Method tho inform the project manager about something
        ...
        Attributes
        ----------
        project : Project
            project , employee working on
        employee : Employee
            employee that have a request
        assignment_managager : AssignmentManager
            manager who will unsign employee from the project
        """

        project.remove_employee(employee, assignment_managager)

    def calculate_salary(self, specific_employee: Employee, task_number: int) -> None:
        """A method used to calculate employee`s salary
           -----------
           Parameters
           specific_employee : Employee
                An employee you want to calculate salary for
            task_number : int
                number of the task done by this specific employee in any project"""

        if task_number == 1:
            return Employee.personal_info.salary
        else:
            return int((Employee.personal_info.salary / 2) * task_number)


class QualityAssurance(Employee):
    """Represintation of Quality Assurance
        ...
        Attributees
        -----------
        None
    """

    def calculate_salary(self, employee_salary: int, task_number: int) -> None:
        """A method used to calculate employee`s salary
           -----------
           Parameters
           employee_salary : int
                salary of specific employee
            task_number : int
                number of the task done by this specific employee in any project"""

        if task_number == 1:
            return employee_salary
        else:
            return int((employee_salary / 2) * task_number)

    def ask_sick_leave(self, project_manager: ProjectManager, project: Project, employee: Employee,
                       assignment_managager: AssignmentManager):
        """A method used to unsign an employee from project becouse of health problem/s
           -----------
           Parameters
           project_manager : ProjectManager
                Project manager asked to unsign employee
           project : Project
                Project employee working on currently
           employee : Employee
                A employee who need to leave
           assignment_managager : AssignmentManager
                manager who will unsign employee from the project
        """

        project_manager.employee_request(project, employee, assignment_managager)


class Team:
    """
        Representation of team of few employees
            ...
        Attributes
        -----------
        None
    """

    def __init__(self, id: uuid.UUID, title: str, member_list: list[uuid.UUID], project_id: uuid.UUID) -> None:
        """A method to create a team to work on on specific project
            -----------
            Parameters
            id : uuid.UUID
                id of team
            title : str
                title/name of the team
            member_list : list(uuid.UUID)
                list of the id`s of specific employee , who will be a part of the team
            project_id : uuid.UUID
                id of the project team workes on
        """
        self.id = id
        self.title = title
        self.member_list = member_list
        self.project_id = project_id


class SoftwareArchitect(Employee):
    """ Represintation of Software Architect
           ...
        Attributes
        _id : int
            id of the developer
        full_name : str
            name and surname of the developer
        address : str
            relevant address
        email : str
            e-mail for work
        phone_number : str
            phone number for work
        position : str
            current position at the company
        salary : str
            income
        ----------
    """

    def __init__(self, id: uuid.UUID, full_name: str, address: str, phone_number: str, email: str, position: str,
                 salary: str) -> None:
        """
        Method to add a developer
        ----------
        _id : int
            id of the developer
        full_name : str
            name and surname of the developer
        address : str
            relevant address
        email : str
            e-mail for work
        phone_number : str
            phone number for work
        position : str
            current position at the company
        salary : str
            income
        """
        self.id = id
        super().__init__(full_name=full_name, address=address, email=email, salary=salary, phone_number=phone_number,
                         position=position)

    def fill_project(self, team: Team) -> None:
        pass

    @abstractmethod
    def create_project(*args) -> Project:
        """Method to create web/embanded/mobile project"""
        pass


class WebArchitect(SoftwareArchitect):
    """ Represintation of Web Architect
           ...
        Attributes
        _id : int
            id of the developer
        full_name : str
            name and surname of the developer
        address : str
            relevant address
        email : str
            e-mail for work
        phone_number : str
            phone number for work
        position : str
            current position at the company
        salary : str
            income
        ----------
    """

    def __init__(self, id: uuid.UUID, full_name: str, address: str, phone_number: str, email: str, position: str,
                 salary: str) -> None:
        """
        Method to add a developer
        ----------
        _id : int
            id of the developer
        full_name : str
            name and surname of the developer
        address : str
            relevant address
        email : str
            e-mail for work
        phone_number : str
            phone number for work
        position : str
            current position at the company
        salary : str
            income
        """
        self.id = id
        super().__init__(full_name=full_name, address=address, email=email, salary=salary, phone_number=phone_number,
                         position=position)

    def create_project(self, id: uuid.UUID, title: str, start_date: datetime, task_list: list[int], limit: int,
                       web_framework: str) -> Project:
        """Method to create web project
            ----------
        _id : uuid.UUID
            id of the developer
        title : str
            name of the project
        start_time : datatime
            time when project should be started
        task_list : list[int]
            list of the ids of the tasks included
        limit : int
            max number of the debelopers included to the project
        """
        return Web(id=id, title=title, start_date=start_date, task_list=task_list, limit=limit,
                   web_framework=web_framework)


class MobileArchitect(SoftwareArchitect):
    """ Represintation of Mobile Architect
           ...
        Attributes
        _id : int
            id of the developer
        full_name : str
            name and surname of the developer
        address : str
            relevant address
        email : str
            e-mail for work
        phone_number : str
            phone number for work
        position : str
            current position at the company
        salary : str
            income
        ----------
    """

    def __init__(self, id: uuid.UUID, full_name: str, address: str, phone_number: str, email: str, position: str,
                 salary: str) -> None:
        """
        Method to add a developer
        ----------
        _id : int
            id of the developer
        full_name : str
            name and surname of the developer
        address : str
            relevant address
        email : str
            e-mail for work
        phone_number : str
            phone number for work
        position : str
            current position at the company
        salary : str
            income
        """
        self.id = id
        super().__init__(full_name=full_name, address=address, email=email, salary=salary, phone_number=phone_number,
                         position=position)

    def create_project(self, id: uuid.UUID, title: str, start_date: datetime, task_list: list[int], limit: int,
                       mobile_framework: str) -> Project:
        """Method to create web project"""
        return Mobile(id=id, title=title, start_date=start_date, task_list=task_list, limit=limit,
                      mobile_framework=mobile_framework)


class EmbeddedArchitect(SoftwareArchitect):
    """ Represintation of Embedded Architect
           ...
        Attributes
        _id : int
            id of the developer
        full_name : str
            name and surname of the developer
        address : str
            relevant address
        email : str
            e-mail for work
        phone_number : str
            phone number for work
        position : str
            current position at the company
        salary : str
            income
        ----------
    """

    def __init__(self, id: uuid.UUID, full_name: str, address: str, phone_number: str, email: str, position: str,
                 salary: str) -> None:
        """
        Method to add a developer
        ----------
        _id : int
            id of the developer
        full_name : str
            name and surname of the developer
        address : str
            relevant address
        email : str
            e-mail for work
        phone_number : str
            phone number for work
        position : str
            current position at the company
        salary : str
            income
        """
        self.id = id
        super().__init__(full_name=full_name, address=address, email=email, salary=salary, phone_number=phone_number,
                         position=position)

    def create_project(self, id: uuid.UUID, title: str, start_date: datetime, task_list: list[int], limit: int,
                       embedded_framwork: str) -> Project:
        """Method to create web project"""
        return Embedded(id=id, title=title, start_date=start_date, task_list=task_list, limit=limit,
                        embedded_framwork=embedded_framwork)