import React from "react"

export default function CustomerSignUp() {
   
    return (
        <div className= "pageBackground">
            <div className= "pageLayout">
                <h1>Sign Up</h1>
                <p className="signInInstruction"> Please enter your login details so we may retrieve your infomation and assist you.</p>
                
                <div className = "signUpStructure">
                    <p className="signInEmail">Email: </p>
                    <input type ="text" className="signInText" placeholder="email"></input>
                    <p className="signInLabel">Password: </p>
                    <input type ="text" className="signInText" placeholder="password" ></input>
                    <p className="signInLabel">Name: </p>
                    <input type ="text" className="signInText" placeholder="Given and last names" ></input>
                    <p className="signInLabel">Address: </p>
                    <input type ="text" className="signInText"  placeholder="address"></input>
                    <p className="signInLabel">Date of Birth: </p>
                    <input type ="text" className="signInText"  placeholder="dd/mm/yy"></input>
                    <button className="createAccount">Create account</button>
                </div>
                
               
                
                
            </div>
            
        </div>
    )
}