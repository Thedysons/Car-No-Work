import React from "react"
import {useNavigate} from "react-router-dom"

export default function MechanicSignIn(props) {
    const navigate= useNavigate()

    function signIn() {
        navigate("/MechanicHomePage")
        props.changeUser("mechanic")
    }

    function signUp() {
        navigate("/MechanicSignUp")
    }

    return (
        <div className= "pageBackground">
            <div className= "cusFormLayout">
            <h1>Sign In</h1>
            <p className="signInInstruction"> Please enter your login details so we may retrieve your <br></br>infomation and assist you.</p>
                <form className = "signInStructure">                
                    <p className="signInLabel">Email: </p>
                    <input type ="text" className="signInText" placeholder="enter email"></input>
                    <p className="signInLabel">Password: </p>
                    <input type ="text" className="signInText" placeholder="enter password" ></input>
                    
                </form>
                <button className="submitButton" onClick={signIn} >Sign In</button>
                <p className="signInInstruction" onClick={signUp}> Dont have an account? Sign up</p>                 
            </div>
        </div>
    )
}
