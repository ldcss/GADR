# Implement Clean Architecture


## Context

This project is meant to be a playground to experiment with different technologies and design solutions.


## Decision

To standardize the project structure, now that it's getting bigger, we will implement the principles suggested by [clean architecture](https://github.com/michelezamuner/notes/tree/master/software-architecture/clean-architecture/clean-architecture.martin), enhanced by concepts from Domain Driven Design, and plugin architectures. 

### Domain
The core domain is the "virtual machine framework", which only defines how programs should be executed, but doesn't specify any architecture, meaning that how programs are interpreted is not known.

A Program is a sequence of Data Units. Data Units are the kind of data with the smallest possible size, which we set at a single Byte. Data is always represented as a sequence of Data Units. Since we work with sequences, we also define the concepts of Size, which is the number of Data Units in a specific Data, and Address of a Data inside the Program, with the Address of the first Data Unit being 0. Both Size and Address are Integers, which is a generic integral type defined to be independent from the runtime environment implementation. A Program has the ability of fetching blocks of Data given their Address and Size.

A Program is run by a Processor, which uses an Interpreter, whose implementation is provided by the specific Architecture selected, to first define which sets of Data Units should be regarded as Instructions, and then to execute these Instructions. When running an Instruction, the Interpreter returns a Status object knowing if the execution should jump, or be terminated. The execution of a Program by a Processor always returns an Exit Status, which is Architecture-dependent. The termination of a Program must always be requested explicitly, via a dedicated instruction, otherwise an error is raised.

An Interpreter must use the System to perform I/O operations, and ultimately to allow a Program to communicate with the users; however, the implementation of the System depends on the actual application where the Processor and Interpreter are running, so it's left to be specified.

Additional domains are defined for each architecture, so that a virtual machine can support many different architectures.

Assemblers and compilers also define their own domains.

The following domains could thus be defined:
- `smf`: the core virtual machine framework domain
- `sma`: definitions for the SMA architecture domain
- `basm`: definitions for the BASM assembler domain
- `php`: definitions for the PHP compiler domain

### Application
The application layer may define the following primary ports:
- the `vm` port allows to execute programs, according to the configured architecture
- the `repl` port allows to execute programs interactively, and uses the functionality of `vm`
- the `dbg` port allows to execute programs step by step for debugging, and uses the functionality of `vm`
- the `asm` port allows to run an assembler on some assembly code to produce executable object code
- the `cmp` port allows to run a compiler on some high level language to produce assembly code

As far as secondary ports, we need the following:
- a `arcl` port allows the application to load an architecture definition
- a `pl` port allows the application to load a program
- a `asml` port allows the application to load assembly code, to be assembled
- a `cl` port allows the application to load high level code, to be compiled
- a `sys` port allows the application to interact with the underlying operating system


### Adapters
Primary adapters might be defined to create command line applications, or Web applications. Secondary adapters might be defined to read data from files or from memory. See below for more concrete examples.


### Plugin architecture
We want to support building different types of applications by composing together sets of different available plugins. For example:

**sloth machine (CLI)**

    AD_sm + AD_larcl + AD_fpl + AD_ossys + AP_vm + AP_arcl + AP_pl + AP_sys + D_smf + D_sma (or others)
    
**sloth machine assembler (CLI)**

    AD_asm + AD_fasml + AP_asm + AP_asml + D_basm (or others)
    
**sloth machine compiler (CLI)**

    AD_cmp + AD_fcl + AD_masml + AP_cmp + AP_asm + AP_cl + AP_asml + D_basm (or others) + D_php (or others)
    
**sloth machine runner (CLI)**

    AD_run + AD_larcl + AD_fcl + AD_masml + AD_mpl + AD_ossys + AP_vm + AP_cmp + AP_asm + AP_arcl + AP_cl + AP_asml + AP_pl + AP_sys + D_smf + D_sma (or others) + D_basm (or others) + D_php (or others)

**sloth machine REPL (CLI)**

    AD_repl + AD_larcl + AD_mcl + AD_masml + AD_mpl + AD_ossys + AP_repl + AP_cmp + AP_asm + AP_arcl + AP_cl + AP_asml + AP_pl + AP_sys + D_smf + D_sma (or others) + D_basm (or others) + D_php (or others)

**sloth machine debugger (CLI)**

    AD_dbg + AD_larcl + AD_fcl + AD_masml + AD_mpl + AD_ossys + AP_dbg + AP_cmp + AP_asm + AP_arcl + AP_cl + AP_asml + AP_pl + AP_sys + D_smf + D_sma (or others) + D_basm (or others) + D_php (or others)
    
**sloth machine Web (Web)**

    AD_web + AD_warcl + AD_wcl + AD_masml + AD_mpl + AD_wsys + AP_vm + AP_cmp + AP_asm + AP_repl + AP_dbg + AP_arcl + AP_cl + AP_asml + AP_pl + AP_sys + D_smf + D_sma (or others) + D_basm (or others) + D_php (or others)

- `D_smf`: Domain Sloth Machine Framework
- `D_sma`: Domain Sloth Machine Architecture
- `D_basm`: Domain Basic Assembly for Sloth Machine
- `D_php`: Domain PHP
- `AP_vm`: Application Virtual Machine (primary port)
- `AP_cmp`: Application Compiler (primary port)
- `AP_asm`: Application Assembler (primary port)
- `AP_repl`: Application REPL (primary port)
- `AP_dbg`: Application Debugger (primary port)
- `AP_arcl`: Application Architecture Loader (secondary port)
- `AP_pl`: Application Program Loader (secondary port)
- `AP_asml`: Application Assembly Loader (secondary port)
- `AP_cl`: Application Code Loader (secondary port)
- `AP_sys`: Application System (secondary port)
- `AD_sm`: Adapter Sloth Machine (primary adapter)
- `AD_cmp`: Adapter Compiler (primary adapter)
- `AD_run`: Adapter Runner (primary adapter)
- `AD_repl`: Adapter REPL (primary adapter)
- `AD_dbg`: Adapter Debugger (primary adapter)
- `AD_web`: Adapter Web (primary adapter)
- `AD_larcl`: Adapter Local Architecture Loader (secondary adapter)
- `AD_warcl`: Adapter Web Architecture Loader (secondary adapter)
- `AD_fpl`: Adapter File Program Loader (secondary adapter)
- `AD_mpl`: Adapter Memory Program Loader (secondary adapter)
- `AD_fasml`: Adapter File Assembly Loader (secondary adapter)
- `AD_masml`: Adapter Memory Assembly Loader (secondary adapter)
- `AD_fcl`: Adapter File Code Loader (secondary adapter)
- `AD_mcl`: Adapter Memory Code Loader (secondary adapter)
- `AD_wcl`: Adapter Web Code Loader (secondary adapter)
- `AD_ossys`: Adapter OS System (secondary adapter)
- `AD_wsys`: Adapter Web System (secondary adapter)


### Example modules
```
domain
    smf
        data
            DataUnit: (Byte)
            Data: DataUnit[]
            Size: (Integer)
            Address: (Integer)
        program [data]
            Program
                Program(data.Data)
                read(data.Address, data.Size): data.Data
        interpreter [data]
            Opcode: data.Data
            Operands: data.Data
            ExitStatus: (Integer)
            Instruction
                Instruction(Address, Opcode, Operands)
                getAddress(): Address
                getOpcode(): Opcode
                getOperands(): Operands
            Status
                shouldJump(): (Boolean)
                getJumpAddress(): data.Address
                shouldExit(): (Boolean)
                getExitStatus(): ExitStatus
            <Interpreter>
                getOpcodeSize(): data.Size
                getOperandsSize(Opcode): data.Size
                exec(Instruction): Status
        processor [program, interpreter]
            Processor
                Processor(interpreter.<Interpreter>)
                run(program.Program): interpreter.ExitStatus
        architecture [data, interpreter]
            <System>
                read(data.Integer fd, data.Size size): data.Data
                write(data.Integer fd, data.Data data, data.Size size): data.Size
            <Architecture>
                getInterpreter(<System>): interpreter.<Interpreter>
    sma [smf]
        Interpreter: smf.interpreter.<Interpreter>
            Interpreter(smf.architecture.<System>)
application
    vm
        run_program [domain.smf, application.arcl, application.pl, application.sys]
            <Request>
                getArchitectureName(): String
                getProgramReference(): String
            Response
                getExitStatus(): domain.smf.interpreter.ExitStatus
            <Presenter>
                present(Response)
            RunProgram
                RunProgram(ProcessorFactory, <Presenter>, application.arcl.<ArchitectureLoader>, application.pl.<ProgramLoader>, application.sys.<System>)
                exec(<Request>)
            ProcessorFactory
                create(domain.smf.interpreter.<Interpreter>): domain.smf.processor.Processor
    arcl [domain.smf]
        <ArchitectureLoader>
            load(architectureName: String): domain.smf.architecture.<Architecture>
    pl [domain.smf]
        <ProgramLoader>
            load(programReference: String): domain.smf.program.Program
    sys [domain.smf]
        <System>: domain.smf.architecture.<System>
adapters
    sm [application.vm, domain.smf]
        run_program [application.vm, domain.smf]
            Request: application.vm.run_program.<Request>
            Controller
                Controller(application.vm.run_program.RunProgram)
                runProgram(Request)
            ViewModel
                ViewModel(domain.smf.interpreter.<ExitStatus>)
                getExitStatus(): <native-integer>
            <View>
                render(ViewModel)
            ExitStatusView: <View>
                render(ViewModel)
                getExitStatus(): <native-integer>
            Presenter: application.vm.run_program.<Presenter>
                Presenter(<View>)
                present(application.vm.run_program.Response)
    larcl [application.arcl]
        LocalArchitectureLoader: application.arcl.<ArchitectureLoader>
    fpl [application.pl]
        FileProgramLoader: application.pl.<ProgramLoader>
    ossys [application.sys]
        OSSystem: application.sys.<System>
```

### Examples of main implementations
```
module domain.smf.processor

import domain.smf.interpreter.<Interpreter>
import domain.smf.program.Program
import domain.smf.interpreter.ExitStatus
import domain.smf.data.Size
import domain.smf.data.Address
import domain.smf.interpreter.Opcode
import domain.smf.interpreter.Operands
import domain.smf.interpreter.Instruction
import domain.smf.interpreter.Status

class Processor
    Processor(<Interpreter> interpreter)
        this.interpreter = interpreter
        
    run(Program program): ExitStatus
        Size opcodeSize = interpreter.getOpcodeSize()
        Address address = 0
        
        while (true)
            Opcode opcode = program.read(address, opcodeSize)
            Size operandsSize = interpreter.getOperandsSize(opcode)
            Address operandsAddress = address + opcodeSize
            Operands operands = program.read(operandsAddress, operandsSize)
            Instruction instruction = new Instruction(address, opcode, operands)
            
            Status status = interpreter.exec(instruction)
            if (status.shouldExit())
                return status.getExitStatus()
            address = status.shouldJump() ? status.getJumpAddress() : operandsAddress + operandsSize
            
        // @todo: handle missing exit
```
```
module domain.sma.interpreter

import domain.smf.interpreter.<Interpreter>
import domain.smf.interpreter.ExitStatus
import domain.smf.interpreter.Status
import domain.smf.data.Size
import domain.smf.data.Address
import domain.smf.interpreter.Opcode
import domain.smf.interpreter.Instruction
import domain.smf.architecture.<System>
import domain.sma.InstructionSet
import domain.sma.Result
import domain.sma.JumpResult
import domain.sma.ExitResult
import domain.sma.InstructionDefinition

class Interpreter: <Interpreter>
    Interpreter(InstructionSet instructionSet, <System> system)
        this.instructionSet = instructionSet
        this.system = system
        
    getOpcodeSize(): Size
        return new Integer(1)
        
    getOperandsSize(Opcode opcode): Size
        return instructionSet.getInstructionDefinition(opcode).getOperandsSize()
        
    exec(Instruction instruction): Status
        Address jumpAddress = null
        Address exitStatus = null
        
        InstructionDefinition definition = instructionSet.getInstructionDefinition(instruction.getOpcode())
        Result result = definition.exec(instruction.getOperands())
        
        if (result instanceof JumpResult)
            jumpAddress = result.getJumpAddress()
            
        if (result instanceof ExitResult)
            exitStatus = result.getExitStatus()

        return new Status(jumpAddress, exitStatus)
```
```
module application.vm.run_program

import application.vm.run_program.ProcessorFactory
import application.vm.run_program.<Presenter>
import application.arcl.<ArchitectureLoader>
import application.pl.<ProgramLoader>
import application.sys.<System>
import application.vm.run_program.<Request>
import domain.smf.architecture.<Architecture>
import domain.smf.interpreter.<Interpreter>
import domain.smf.processor.Processor
import domain.smf.program.Program
import domain.smf.interpreter.ExitStatus
import application.vm.run_program.Response

class RunProgram
    RunProgram(
        ProcessorFactory processorFactory,
        <Presenter> presenter,
        <ArchitectureLoader> architectureLoader,
        <ProgramLoader> programLoader,
        <System> system
    )
        this.processorFactory = processorFactory
        this.presenter = presenter
        this.architectureLoader = architectureLoader
        this.programLoader = programLoader
        this.system = system

    exec(<Request> request)
        <Architecture> architecture = architectureLoader.load(request.getArchitectureName())
        <Interpreter> interpreter = architecture.getInterpreter(this.system)
        Processor processor = processorFactory.create(interpreter)
        
        Program program = programLoader.load(request.getProgramReference())
        ExitStatus exitStatus = processor.run(program)
        presenter.present(new Response(exitStatus))
```
```
module adapters.sm.run_program

import application.vm.run_program.RunProgram
import application.vm.run_program.<Request>

class Controller
    Controller(RunProgram service)
        this.service = service

    runProgram(<Request> request)
        service.run(request)
```
```
module adapters.sm.run_program

import adapters.sm.run_program.<View>
import application.vm.run_program.Response
import adapters.sm.run_program.ViewModel

class Presenter
    Presenter(<View> view)
        this.view = view
        
    present(Response response)
        ViewModel viewModel = new ViewModel(response.getExitStatus())
        view.render(viewModel)
```


## Status

Proposed


## Consequences

Modules and source files will be created according to the architectural structure described.
