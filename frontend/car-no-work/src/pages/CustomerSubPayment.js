import React from "react"

export default function CustomerSubPayment() {
    return (
    <div className = "pageBackground">
        <div className ="pageLayout">
        <p className="signInLabel">Card number </p>
        <input type="text" placeholder="enter card number" className="signInText"></input>
        <p className="signInLabel">Card Expiry </p>
        <input type="text" placeholder="mm/yyyy" className="signInText"></input>
        <p className="signInLabel">cvc </p>
        <input type="text" placeholder="Enter cvc" className="signInText"></input>
        <button>Submit</button>   
        </div>        
    </div>
    )
}