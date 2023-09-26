# Tables as Code: The Journey from Ad-hoc Scripts to Maintainable ETL Workflows at Booking.com
by Bram van den Akker, Jon Smith
* [Talk info](https://amsterdam2023.pydata.org/cfp/talk/LKTDB3/)
* [Slides](https://docs.google.com/presentation/d/e/2PACX-1vTHXpCyfo8zzzRm8yWpHqBmU2DS34jbOiQt7BK--Asqn7Y627I3Ss_AJrLm5K76-boyGOtSu_1MNMDj/pub?start=false&loop=false&delayms=3000)
* [Slides in pdf](./slides.pdf)

## Abstract
Until a few years ago, data science & engineering at Booking.com had grown largely in an ad-hoc manner. This growth has led to a labyrinth of unrelated scripts representing Extract-Transform-Load (ETL) processes. Without options for quickly testing cross-application interfaces, maintenance and contribution grew unwieldy, and debugging in production was a common practice.

Over the past several years, we’ve spearheaded a transition from isolated workflows to a well-structured community-maintained monorepo - a task that required not just technical adaptation, but also a cultural shift.

Central to this transformation is the adoption of the concept of "tables as code", an approach that has changed the way we write ETL. Our lightweight PySpark extension represents table metadata as a Python class, exposing data to code, and enabling efficient unit test setup and validation.

In this talk, we walk you through “tables as code” design and complementary tools such as efficient unit testing, robust telemetry, and automated builds using Bazel. Moreover, we will cover the transformation process, including enabling people with non-engineering backgrounds to create fully tested and maintainable ETL. This includes internal training, maintainers, and support strategies aimed at fostering a community knowledgeable in best practices.
