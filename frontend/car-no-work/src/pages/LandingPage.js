import React from 'react';

class LandingPage extends React.Component {
  
  render(){
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
}


