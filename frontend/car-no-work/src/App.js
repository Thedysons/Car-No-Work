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
import PlansAndPrices from "./pages/PlansAndPrices";

function App() {  
    const [userType, setUserType] = React.useState("")
    

    const [dummyCustomer, setDummyCustomer] = React.useState(
    {
        email: "user@email.com",
        password: "pw",
        name: "John Doe",
        Address: "123 Fake Street, Realtown",
        DateOfBirth: "22/06/2000"
    })

  

    const [dummyMechanic, setDummyMechanic] = React.useState( 
    {
        email: "user@mechanic.com",
        password: "pw",
        name: "Bob Doe",
        Address: "123 Fake Street, Realtown",
        DateOfBirth: "22/06/2002",
        NumberPlate: "22-FF-66",
        carModel: "toyota"
    })
      
    return (
        <BrowserRouter>
            <div>
                <div className="App">
                    <NavBar user={userType}/>
                    <div>
                        <Routes>
                            {/* add routes, unordered atm */}
                            <Route path="/RapProfilePage" element={<RapProfilePage
                                                            mech = {dummyMechanic} />} />  
                            <Route path="/*" element={<LandingPage changeUser={userType=> setUserType(userType)}/>} />   
                            <Route path="/SignIn" element={<SignIn 
                                        changeUser={userType => setUserType(userType)}
                                        customer={dummyCustomer}                                        
                                        />} />
                            <Route path="/CustomerHome" element={<CustomerHome />} />                                                           
                            <Route path="/RapProfilePage" element={<RapProfilePage />} /> 
                            <Route path="/SignUp" element={<CustomerSignUp 
                                                                customer={dummyCustomer}
                                                                />} /> 
                            <Route path="/customerSubscriptionPayment" element={<CustomerSubPayment />} /> 
                            <Route path="/guestCustomerPayment" element={<GuestCustomerPayment />} /> 
                            <Route path="/MechanicSignUp" element={<MechanicSignUp />} /> 
                            <Route path="/MechanicHomePage" element={<MechanicHomePage />} /> 
                            <Route path="/CustomerProfile" element={<CustomerProfile />} /> 
                            <Route path="/MechanicSignIn" 
                                element={<MechanicSignIn changeUser={userType => setUserType(userType)}
                                                        mech = {dummyMechanic}/>} /> 

                            <Route path="/PlansAndPrices" element={<PlansAndPrices/>} />

                        </Routes>
                    </div>
                </div>
                
            </div>
        </BrowserRouter>
    
    )

}
export default App;

        
    
