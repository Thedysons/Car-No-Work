import React from "react"
import { useNavigate } from "react-router-dom";
import CustomerSignUp from "./CustomerSignUp";

export default function SignIn(props) {
    const [email, setEmail] = React.useState("")
    const [password, setPassword] = React.useState("")
    const navigate = useNavigate();

    function signIn() {
        if(email === props.customer.email && password === props.customer.password) {
        navigate("/CustomerHome")
        props.changeUser("member")
        }
    }   

    function SignUp() {
        navigate("/SignUp")
    }

    function handleEmail(e) {
        setEmail(e.target.value)
    }

    function handlePassword(e) {
        setPassword(e.target.value)
    }


    return (
        <div className= "pageBackground">
            <div className= "cusFormLayout">
            <h1>Sign In</h1>
            <p className="signInInstruction"> Please enter your login details so we may retrieve your <br></br>infomation and assist you.</p>
                <form className = "signInStructure">                
                    <p className="signInLabel">Email: </p>
                    <input type ="text" className="signInText" placeholder="enter email" onChange={handleEmail}></input>
                    <p className="signInLabel">Password: </p>
                    <input type ="text" className="signInText" placeholder="enter password" onChange={handlePassword} ></input>
                    
                </form>
                <button className="submitButton" onClick ={signIn}>Sign In</button>
                <p className="signInInstruction" onClick={SignUp}> Dont have an account? Sign up</p>                 
            </div>
        </div>
    )
}

//sign up must make hyperlink