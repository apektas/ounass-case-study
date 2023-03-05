import React, {useEffect, useState} from "react";
import {FaPlus} from 'react-icons/fa';
import {Card, Tooltip} from "antd";
import {getAdsetInsight, getAdsets} from "../../services/services";
import {useLocation, useNavigate} from "react-router-dom";
import DialogWithNoFooter from "../../components/modal/DialogWithNoFooter";
import AddAdsetForm from "./components/AddAdsetForm";
import DialogWithFooter from "../../components/modal/DialogWithFooter";

const AdSet = () => {
    const navigate = useNavigate();
    const location = useLocation();
    const [insightData, setInsightData] = useState("");
    const [adsets, setAdsets] = useState([]);
    const [visible, setVisible] = useState(false);
    const [insightVisible, setInsightVisible] = useState(false);

    let campaignId = location.pathname.split("/")[2];

    const adsetData = () => {
        getAdsets().then((response) => {
            if(response?.data !== null) {
                setAdsets(response?.data.filter(data => data.campaign_id === campaignId));
            }
            return response;
        });
    }

    const insight = async (adsetID) => {
        getAdsetInsight(adsetID).then((response) => {
            if(response?.data !== null) {
                setInsightData(response.data);
            }
            return response;
        });
    }

    const insightOnClick = (adsetID) => {
        insight(adsetID);
        setInsightVisible(true);
    }

    useEffect(() => {
        adsetData();
    }, []);

    return (
        <div>
            <h1>Adsets</h1>
            <DialogWithNoFooter
                key="dialog"
                title="Add Adset"
                visible={visible}
                onOk={() => {setVisible(false)}}
                onCancel={() => {setVisible(false)}}
            >
                <AddAdsetForm key={"addAdsetForm"} campaign_id={campaignId} setVisible={setVisible} adsetData={adsetData}/>
            </DialogWithNoFooter>
            <DialogWithFooter
                key="dialogInsight"
                title="Insight"
                visible={insightVisible}
                width={400}
                onOk={() => {setInsightVisible(false)}}
                onCancel={() => {setInsightVisible(false)}}
            >
                <div>
                    <div>
                        <span style={{marginRight:"10px"}}><b>Impressions:</b></span>
                        <span>{insightData.insights?.impressions}</span>
                    </div>
                    <div>
                        <span style={{marginRight: "10px"}}><b>Clicks:</b></span>
                        <span>{insightData.insights?.clicks}</span>
                    </div>
                </div>

            </DialogWithFooter>

            <div style={{display: "flex", textAlign: "start", alignItems:"center", flexWrap: "wrap"}}>
                {adsets?.map((adset, index) => (
                    <div key={"card"+index} style={{display: "inline-block"}}>
                        <Tooltip title={adset.name} placement="rightTop" mouseEnterDelay={1} color="#001529">
                            <Card
                                key={adset.id}
                                title={adset.name}
                                extra={<a onClick={()=>insightOnClick(adset.id)}>Insight</a>}
                                bordered={true}
                                hoverable={true}
                                style={{
                                    width: 300,
                                    height: 320,
                                    margin: 30
                                }}
                            >
                                <div onClick={()=> navigate("/campaign/" + campaignId + "/adset/" + adset.id + "/ads")}>
                                    <div>
                                        <span style={{marginRight:"10px"}}><b>ID:</b></span>
                                        <span>{adset.id}</span>
                                    </div>
                                    <div>
                                        <span style={{marginRight: "10px"}}><b>Daily Budget:</b></span>
                                        <span>{adset.daily_budget}</span>
                                    </div>
                                    <div>
                                        <span style={{marginRight: "10px"}}><b>Duration (days):</b></span>
                                        <span>{adset.ends_after}</span>
                                    </div>
                                    <div>
                                        <span style={{marginRight: "10px"}}><b>Bid Amount:</b></span>
                                        <span>{adset.bid_amount}</span>
                                    </div>
                                    <div>
                                        <span style={{marginRight: "10px"}}><b>Billing Event:</b></span>
                                        <span>{adset.billing_event}</span>
                                    </div>
                                    <div>
                                        <span style={{marginRight: "10px"}}><b>Optimization Goal:</b></span>
                                        <span>{adset.optimization_goal}</span>
                                    </div>
                                    <span><b>Target Audience:</b></span>
                                    <div>
                                        <span style={{margin: "0 10px 0 20px"}}>- Min Age:</span>
                                        <span>{adset.targeting?.age_min}</span>
                                    </div>
                                    <div>
                                        <span style={{margin: "0 10px 0 20px"}}>- Max Age:</span>
                                        <span>{adset.targeting?.age_max}</span>
                                    </div>
                                    <div>
                                        <span style={{margin: "0 10px 0 20px"}}>- Countries:</span>
                                        {
                                            adset.targeting?.geo_locations?.countries?.map((country, idx) => (
                                                <span key={country + idx} style={{marginRight: "10px"}}>{country}</span>
                                            ))
                                        }
                                    </div>
                                </div>
                            </Card>
                        </Tooltip>
                    </div>
                ))}
                <div style={{display: "inline-block", textAlign: "center"}}>
                    <Card onClick={()=> setVisible(true)}
                          key="add"
                          hoverable={true}
                          style={{
                              width: 300,
                              height: 320,
                              margin: 30
                          }}
                    >
                        <div style={{marginTop: "110px"}}>
                            <p>Click Here to Add New Advertisement Set</p>
                            <FaPlus />
                        </div>
                    </Card>
                </div>
            </div>
        </div>
    );
};

export default AdSet;
