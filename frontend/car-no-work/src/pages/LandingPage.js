import React from 'react'
import { useNavigate } from "react-router-dom"



export default  function LandingPage(props) {

  const navigate =useNavigate()

  function changePage(e) {
    
    if(e.target.value === "mechanic") {
      navigate("/MechanicSignIn")
    } else if (e.target.value === "guest") {
      navigate("/CustomerHome")
      props.changeUser("guest")
    }  else if (e.target.value === "member") {
       navigate("/SignIn")
    }          
  } 
 
  return (
    <div>
     

      <div className = "landingPage">        
        <div className = "MechanicLanding">
          <button value="mechanic" onClick={changePage} ><h1>Mechanic</h1></button>
        </div>
        <div className = "CustomerLanding">
          <button value="member" onClick={changePage}><h1>Member</h1></button>
        </div>
        <div className = "GuestLanding">
          <button value="guest" onClick={changePage}><h1>Guest</h1></button>
        </div>
      </div>
     
    </div>
  )
}


