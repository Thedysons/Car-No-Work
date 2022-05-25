import React from "react"

export default function SignUp() {
    return (
        <div className= "pageBackground">
            <div className= "pageLayout">
                <h1>Sign In</h1>
                <p className="signInInstruction"> Please enter your login details so we may retrieve your infomation and assist you.</p>
                <p className="signInInstruction"> Dont have an account? Sign up</p> 
                <p className="signInLabel">Email: </p>
                <input type ="text" className="signInText"></input>
                <p className="signInLabel">Password: </p>
                <input type ="text" className="signInText" ></input>
                
            </div>
        </div>
    )
}

//sign up must make hyperlink