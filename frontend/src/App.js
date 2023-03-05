import './App.css';
import React from "react";
import Navbar from "./components/navbar/Navbar";
import {Layout} from "antd";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import NoPage from "./views/NoPage";
import Campaign from "./views/campaignPage/Campaign";
import AdSet from "./views/adsetPage/AdSet";
import AdCreative from "./views/adCreativePage/AdCreative";
import {NotificationContainer} from "react-notifications";
import 'react-notifications/lib/notifications.css';
import Ad from "./views/adPage/Ad";
import {GlobalLoading} from "react-global-loading";

const {Content} = Layout;


function App() {
    return (
        <div className="App">
            <NotificationContainer/>
            <GlobalLoading />
            <BrowserRouter>
                <Layout>
                    <Navbar/>
                    <Content style={{padding: '50px'}}>
                        <div
                            style={{
                                padding: 24,
                                minHeight: "83.9vh",
                                background: "white"
                            }}
                        >
                            <Routes>
                                <Route path="/campaign/:campaignId/adset/:adsetId/ads" element={<Ad/>}/>
                                <Route path="/campaign/:campaignId/adsets" element={<AdSet/>}/>
                                <Route path="/adCreative" element={<AdCreative/>}/>
                                <Route path="/*" element={<NoPage/>}/>
                                <Route path="/" element={<Campaign/>}/>
                            </Routes>
                        </div>
                    </Content>
                </Layout>
            </BrowserRouter>
        </div>
    );
}

export default App;
