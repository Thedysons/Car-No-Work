import React from "react"

export default function CustomerSignUp() {
   
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
                <p className="signInLabel">Name: </p>
                <input type ="text" className="signInText" ></input>
                <p className="signInLabel">Address: </p>
                <input type ="text" className="signInText" ></input>
                <p className="signInLabel">Date of Birth: </p>
                <input type ="text" className="signInText" ></input>
                
               
                <button className="createAccount">Create account</button>
                
            </div>
            
        </div>
    )
}