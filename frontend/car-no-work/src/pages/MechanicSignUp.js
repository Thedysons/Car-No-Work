import React from "react"

export default function MechanicSignIn() {
    return (
    <div className = "pageBackground">
        <div className ="cusFormLayout">
        <h1>Mechanic Sign Up</h1>
                <p className="signInInstruction"> Please enter your login details so we may retrieve your infomation and evaluate your skills.</p>
                <form className = "signUpStructure">
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
                    <p className="signInLabel">Car Number Plate: </p>
                    <input type ="text" className="signInText"  placeholder="enter number plate"></input>
                    <button className="submitButton">Create account</button>
                </form>                
        </div>        
    </div>
    )
}