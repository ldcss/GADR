## Data Access API 

#### Context and Problem Statement

A technology stack is required for the projects data access application programming interface (API).

#### Considered Options

- ASP.NET Web API (C#)

#### Decision Outcome

Chosen option: "ASP.NET Web API (C#)", because

- This can target .Net Core 2
- Dapper Object Relational Mapper (ORM) can be used, leveraging reuse of skills already within Trade Me.
- A repository pattern can be applied facilitating Unit Testing. 



([back](README.md))