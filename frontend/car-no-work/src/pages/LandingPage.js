import React, {useState, useEffect} from 'react';
import {Card} from '../components/Cards/card';

class LandingPage extends React.Component {
  /*the API testing method*/
  useEffect() {
    fetch('/api').then(response => {
      if(response.ok){
        return response.json()
      }
    }).then(data => console.log(data))
  }
  componentDidMount(){
    this.useEffect();
  }
  render(){
  return (
  
    <div className='main'>
      {/* Landing Page*/}
      

      <br/><br/><br/><br/>
      <p>this is the landing page:)</p>
      <Card/>
      
      
    </div>
  )}
}

export default LandingPage
