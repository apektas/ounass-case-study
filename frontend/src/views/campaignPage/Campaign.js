import React, {useEffect, useState} from "react";
import {FaPlus} from 'react-icons/fa';
import {Card, Tooltip} from "antd";
import {useNavigate} from "react-router-dom";
import DialogWithNoFooter from "../../components/modal/DialogWithNoFooter";
import AddCampaignForm from "./components/AddCampaignForm";
import {getCampaigns} from "../../services/services";

const Campaign = () => {
    const navigate = useNavigate();
    const [campaigns, setCampaigns] = useState([]);
    const [visible, setVisible] = useState(false);

    const campaignData = async () => {
        getCampaigns().then((response) => {
            if(response?.data !== null) {
                setCampaigns(response.data);
            }
            return response;
        });
    }

    useEffect(() => {
        campaignData();
    }, []);

    return (
        <div>
            <h1>Campaigns</h1>
            <DialogWithNoFooter
                key="dialog"
                title="Add Campaign"
                visible={visible}
                onOk={() => {setVisible(false)}}
                onCancel={() => {setVisible(false)}}
            >
                <AddCampaignForm key={"addCampaignForm"} setVisible={setVisible} campaignData={campaignData}/>
            </DialogWithNoFooter>

            <div style={{display: "flex", textAlign: "start", alignItems:"center", flexWrap: "wrap"}}>
                {campaigns?.map((campaign, index) => (
                    <div key={"card"+index}  style={{display: "inline-block"}}>
                        <Tooltip title={campaign.name} placement="rightTop" mouseEnterDelay={1} color="#001529">
                            <Card
                                onClick={()=> navigate("/campaign/" + campaign.id + "/adsets")}
                                key={campaign.id}
                                title={campaign.name}
                                bordered={true}
                                hoverable={true}
                                style={{
                                    width: 300,
                                    height: 170,
                                    margin: 30
                                }}
                            >
                                <div>
                                    <span style={{marginRight:"10px"}}><b>ID:</b></span>
                                    <span>{campaign.id}</span>
                                </div>
                                <div>
                                    <span style={{marginRight: "10px"}}><b>Objective:</b></span>
                                    <span>{campaign.objective}</span>
                                </div>
                                <div>
                                    <span style={{marginRight: "10px"}}><b>Status:</b></span>
                                    <span>{campaign.status}</span>
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
                              height: 170,
                              margin: 30
                          }}
                    >
                        <p>Click Here to Add New Campaign</p>
                        <FaPlus />
                    </Card>
                </div>
            </div>
        </div>
    );
};

export default Campaign;
