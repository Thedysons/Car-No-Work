import React from "react"
import {TiTick} from "react-icons/ti"
export default function CustomerHome() {
    return (
        <div className = "pageBackground">
            <div className ="pageLayout">
                <h1>Home</h1>
                <h3>(Customer Name)</h3>
                <p>Enter Crash Details(500 characters)</p>
                <textarea></textarea>
                <button>Request Service</button>
                <span><TiTick/></span>
                <p>distance: </p>
                <p>time:</p>
            </div>
        </div>
    )
}