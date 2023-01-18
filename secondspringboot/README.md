# My Process
#

1. Https//start.spring.io
    - Maven, Java, Spring Boot 3.0.1,
    - group: com.jy.firstspringboot
    - artifact: firstspringboot
    - name: firstspringboot
    - Description: first spring boot
    - Package name: com.jy.firstspringboot.first-spring-boot
    - dependencies added: spring web
2. imported Maven, selected the current project folder
3. Created a HelloWorld class and a Controller Class for HelloWorld
4. Added a request mapping (GET) for /hello-world
5. Created a HelloWorldBean class that returns a JSON format from whatever input
6. Added a GET mapping in Controller class that inputs a specific String when REST API is used

- details: how are our requests handled?
	- all our requests are going to DispatcherServlet - aka Front Controller Pattern
		- Mapping servlets: dispatcherServlet urls=[/]
		- Auto Configuration(DispatcherServletAutoConfiguration)
			- this is what is configuring the dispatcher servlet
- How does HelloWorldBean object get converted to JSON?
	- request goes to dispatcher servlet, dispatcher servlet checks which resources are available, and executes the method
	- @ResponseBody + JacksonHttpMEssageConverters
	- ResponseBody
		- inside the @RestController
		- it tells the bean to return as is based on the method
	- JacksonHttpMessageConverters
		- the default conversion which is setup by spring boot auto configuration
- Who is configuring error mapping?
	- Auto Configuration (ErrorMvcAutoConfiguration)
		
