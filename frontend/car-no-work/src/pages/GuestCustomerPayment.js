import React from "react"
import { FaStar } from "react-icons/fa"

export default function GuestCustomerPayment() {
    return (
    <div className = "pageBackground">
        <div className ="pageLayout">
        <h1>Finalise Transaction</h1>
        <p className="signInLabel">Card number </p>
        <input type="text" placeholder="enter card number" className="signInText"></input>
        <p className="signInLabel">Card Expiry </p>
        <input type="text" placeholder="mm/yyyy" className="signInText"></input>
        <p className="signInLabel">cvc </p>
        <input type="text" placeholder="Enter cvc" className="signInText"></input>

        <p className="signInLabel">How would you rate your experience?</p>
        <div className="Rating">
            <FaStar className = "Star"/>
            <FaStar className = "Star" />
            <FaStar className = "Star" />
            <FaStar className = "Star"/>
            <FaStar className = "Star" />
        </div>
        <p className="signInLabel">Reasons for your score(200 characters)</p>
        <textarea></textarea>

        <button>Submit</button>   
        </div>        
    </div>
    )
}