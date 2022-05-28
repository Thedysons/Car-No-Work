import React from "react"
import {Route, Routes, BrowserRouter} from "react-router-dom"
import NavBar from "./components/NavBar"
import './App.css';
/*pages */
import SignIn from "./pages/SignIn"
import RapProfilePage from "./pages/RapProfilePage"
import LandingPage from "./pages/LandingPage"
import CustomerSignUp from "./pages/CustomerSignUp";
import CustomerSubPayment from "./pages/CustomerSubPayment";
import GuestCustomerPayment from "./pages/GuestCustomerPayment";
import CustomerHome from "./pages/CustomerHome"
import MechanicSignUp from "./pages/MechanicSignUp";
import MechanicHomePage from "./pages/MechanicHomePage";
import CustomerProfile from "./pages/CustomerProfile"
import MechanicSignIn from "./pages/MechanicSignIn";


function App() {  
    const [userType, setUserType] = React.useState("")
    React.useEffect(() => {
        console.log(userType)
});
      
    return (
        <BrowserRouter>
            <div>
                <div className="App">
                    <NavBar user={userType}/>
                    <div>
                        <Routes>
                            {/* add routes, unordered atm */}
                            <Route path="/RapProfilePage" element={<RapProfilePage />} />  
                            <Route path="/*" element={<LandingPage changeUser={userType=> setUserType(userType)}/>} />   
                            <Route path="/SignIn" element={<SignIn changeUser={userType => setUserType(userType)}/>} />
                            <Route path="/CustomerHome" element={<CustomerHome />} />                                                           
                            <Route path="/RapProfilePage" element={<RapProfilePage />} /> 
                            <Route path="/SignUp" element={<CustomerSignUp />} /> 
                            <Route path="/customerSubscriptionPayment" element={<CustomerSubPayment />} /> 
                            <Route path="/guestCustomerPayment" element={<GuestCustomerPayment />} /> 
                            <Route path="/MechanicSignUp" element={<MechanicSignUp />} /> 
                            <Route path="/MechanicHomePage" element={<MechanicHomePage />} /> 
                            <Route path="/CustomerProfile" element={<CustomerProfile />} /> 
                            <Route path="/MechanicSignIn" 
                                element={<MechanicSignIn changeUser={userType => setUserType(userType)}/>} /> 

                        </Routes>
                    </div>
                </div>
                
            </div>
        </BrowserRouter>
    
    )

}
export default App;

        
    
