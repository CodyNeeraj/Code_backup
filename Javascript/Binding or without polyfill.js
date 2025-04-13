let name ={
    firstname: "Rohan",
    lastname : "Mishra is OP !!"
}

let printname = function (testparam,testparam2,testparam3){
    console.log(this.firstname + " "+ this.lastname +" "+ testparam + " "+ testparam2 + " "+ testparam3)
}

let printname1 = printname.bind(name)
// here printname is internally returning a function so do we've to do the same in our custom function
// printname1()


//here this keyword will point out to the function definition of the
// called on function on which custom bind property is applied
// which is printname here !!

Function.prototype.newBindMethod = function (...args){
    let obj = this
    console.log("from custom bind method "+ this)
    return function (){
        obj.call(args[0])
    }
}
