let name ={
    firstname: "Rohan",
    lastname : "Mishra is OP !!"
}

let printname = function (testparam,testparam2,testparam3){
    console.log(this.firstname + " "+ this.lastname +" "+ testparam + " "+ testparam2 + " "+ testparam3)
}

let printname1 = printname.bind(name)

Function.prototype.newBindMethod = function (...args){
    let obj = this
    return function (){
        obj.call(args[0])
    }
}

Function.prototype.newBindMethod = function (...args){
    let obj = this
    let params = args.slice(1)
    console.log("Inside the main method ",params)
}
