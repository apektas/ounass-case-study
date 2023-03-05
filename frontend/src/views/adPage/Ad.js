import React, {useEffect, useState} from "react";
import {FaPlus} from 'react-icons/fa';
import {Card, Tooltip} from "antd";
import DialogWithNoFooter from "../../components/modal/DialogWithNoFooter";
import {getAdPreview, getAds} from "../../services/services";
import AddAdForm from "../adPage/components/AddAdForm";
import {useLocation} from "react-router-dom";
import DialogWithFooter from "../../components/modal/DialogWithFooter";

const Ad = () => {
    const location = useLocation();
    const [ads, setAds] = useState([]);
    const [adPreviewData, setAdPreviewData] = useState("");
    const [visible, setVisible] = useState(false);
    const [previewVisible, setPreviewVisible] = useState(false);

    let adsetId = location.pathname.split("/")[4];

    const adData = async () => {
        getAds().then((response) => {
            if(response?.data !== null) {
                setAds(response.data?.filter(data => data.adset_id === adsetId));
            }
            return response;
        });
    }

    const adPreview = async (adID) => {
        getAdPreview(adID).then((response) => {
            if(response?.data !== null) {
                setAdPreviewData(response.data?.body);
            }
            return response;
        });
    }

    useEffect(() => {
        adData();
    }, []);


    const previewOnClick = (adID) => {
        adPreview(adID);
        setPreviewVisible(true);
    };

    return (
        <div>
            <h1>Ads</h1>
            <DialogWithNoFooter
                key="dialog"
                title="Add Ad"
                visible={visible}
                onOk={() => {setVisible(false)}}
                onCancel={() => {setVisible(false)}}
            >
                <AddAdForm key={"addAdForm"} adset_id={adsetId} setVisible={setVisible} adData={adData}/>
            </DialogWithNoFooter>
            <DialogWithFooter
                key="dialogPreview"
                title="Preview"
                visible={previewVisible}
                width={600}
                onOk={() => {setPreviewVisible(false)}}
                onCancel={() => {setPreviewVisible(false)}}
            >
                {/*{adPreviewData}*/}
                <div dangerouslySetInnerHTML={{__html: "<html><head><title> Facebook Preview</title></head><body>" + adPreviewData + "</body></html>"}} />
            </DialogWithFooter>

            <div style={{display: "flex", textAlign: "start", alignItems:"center", flexWrap: "wrap"}}>
                {ads?.map((ad, index) => (
                    <div key={"card"+index}  style={{display: "inline-block"}}>
                        <Tooltip title={ad.name} placement="rightTop" mouseEnterDelay={1} color="#001529">
                            <Card
                                key={ad.id}
                                title={ad.name}
                                extra={<a onClick={()=>previewOnClick(ad.id)}> Preview</a>}
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
                                    <span>{ad.id}</span>
                                </div>
                                <div>
                                    <span style={{marginRight: "10px"}}><b>Creative ID:</b></span>
                                    <span>{ad.creative?.creative_id}</span>
                                </div>
                                <div>
                                    <span style={{marginRight: "10px"}}><b>Status:</b></span>
                                    <span>{ad.status}</span>
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
                        <p>Click Here to Add New Ad</p>
                        <FaPlus />
                    </Card>
                </div>
            </div>
        </div>
    );
};

export default Ad;
