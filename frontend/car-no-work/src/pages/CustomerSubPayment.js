import React from "react"

export default function CustomerSubPayment() {
    return (
    <div className = "cusFormLayout">
        <div className ="pageLayout">
        <h1>Become a member</h1>
            <form className = "paymentStructure">                
                <p className="signInLabel">Card number </p>
                <input type="text" placeholder="enter card number" className="signInText"></input>
                <p className="signInLabel">Card Expiry </p>
                <input type="text" placeholder="mm/yyyy" className="signInText"></input>
                <p className="signInLabel">cvc </p>
                <input type="text" placeholder="Enter cvc" className="signInText"></input>
                <button className="submitButton">Submit</button>   
            </form>
        </div>        
    </div>
    )
}