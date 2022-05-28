import React from "react"

export default function CustomerSignUp(props) {
    const [email, setEmail] = React.useState("")
    const [password, setPassword] = React.useState("")
    const [name, setName] = React.useState("")
    const [Address, setAddress] = React.useState("")
    const [Dob, setDob] = React.useState("")

    function handleEmail(e) {
        setEmail(e.target.value)
    }
    function handlePassword(e) {
        setPassword(e.target.value)
    }
    function handleName(e) {
        setName(e.target.value)
    }
    function handleAddress(e) {
        setAddress(e.target.value)
    }
    function handleDOB(e) {
        setDob(e.target.value)
    }

    const c = {
        email: email,
        password: password,
        name: name,
        Address: Address,
        DateOfBirth: Dob
    }

    function handleCustomer() {
        props.changeCustomer(c)
    }
    
    function log() {
        console.log(props.customer)
    }
   
    return (
        <div className= "pageBackground">
            <div className= "cusFormLayout">
                <h1>Sign Up</h1>
                <p className="signInInstruction"> Please enter your login details so we may retrieve your infomation and assist you.</p>
                
                <form className = "signUpStructure">
                    <p className="signInEmail">Email: </p>
                    <input type ="text" className="signInText" placeholder="email" onChange ={handleEmail}></input>
                    <p className="signInLabel">Password: </p>
                    <input type ="text" className="signInText" placeholder="password" onChange ={handlePassword}></input>
                    <p className="signInLabel">Name: </p>
                    <input type ="text" className="signInText" placeholder="Given and last names" onChange ={handleName} ></input>
                    <p className="signInLabel">Address: </p>
                    <input type ="text" className="signInText"  placeholder="address" onChange ={handleAddress}></input>
                    <p className="signInLabel">Date of Birth: </p>
                    <input type ="text" className="signInText"  placeholder="dd/mm/yy" onChange ={handleDOB}></input>
                    <button className="submitButton" onClick={handleCustomer}>Create account</button>
                </form>    
               
               <button onClick={log}>temp</button>
                
                
            </div>
            
        </div>
    )
}