import React from "react"
import { FaStar } from "react-icons/fa"
import him from '../img/8f894a44e3cd1a595d547670308eae36.png';
import { Link} from "react-router-dom";

export default function RapProfilePage(props) {
    return (
        <div className= "pageBackground">
            <div className="pageLayout">
                <h1>{props.mech.name}</h1>
                <img src={him} className="RapPhoto" alt='him'/>
                <div className="Rating">
                    <FaStar className = "Star"/>
                    <FaStar className = "Star" />
                    <FaStar className = "Star" />
                    <FaStar className = "Star"/>
                    <FaStar className = "Star" />
                </div>
                <button className="mechProfileButtons">See Reviews</button>
                <div className="infoHold">
                    <div className="RapInfoLabel">
                        <p>Car: </p>
                        <p>LicencePlate: </p>
                        <p>Date of Birth: </p>                        
                    </div>
                    <div>
                    <p> {props.mech.carModel}</p>
                    <p> {props.mech.NumberPlate}</p>
                    <p> {props.mech.DateOfBirth}</p>  

                    </div>
                </div>

                <button className="mechProfileButtons" >Job History</button>
                
                <Link to="/LandingPage">click to go to landing page</Link>
            </div>
        </div>
    )
}