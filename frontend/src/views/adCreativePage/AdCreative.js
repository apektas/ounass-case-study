import React, {useEffect, useState} from "react";
import {FaPlus} from 'react-icons/fa';
import {Card, Tooltip} from "antd";
import DialogWithNoFooter from "../../components/modal/DialogWithNoFooter";
import {getAdCreatives} from "../../services/services";
import AddAdCreativeForm from "./components/AddAdCreativeForm";

const AdCreative = () => {
    const [adCreatives, setAdCreatives] = useState([]);
    const [visible, setVisible] = useState(false);

    const adCreativeData = async () => {
        getAdCreatives().then((response) => {
            if(response?.data !== null) {
                setAdCreatives(response.data);
            }
            return response;
        });
    }

    useEffect(() => {
        adCreativeData();
    }, []);

    return (
        <div>
            <h1>AdCreatives</h1>
            <DialogWithNoFooter
                key="dialog"
                title="Add AdCreative"
                visible={visible}
                onOk={() => {setVisible(false)}}
                onCancel={() => {setVisible(false)}}
            >
                <AddAdCreativeForm key={"addAdCreativeForm"} setVisible={setVisible} adCreativeData={adCreativeData}/>
            </DialogWithNoFooter>

            <div style={{display: "flex", textAlign: "start", alignItems:"center", flexWrap: "wrap"}}>
                {adCreatives?.map((adCreative, index) => (
                    <div key={"card"+index}  style={{display: "inline-block"}}>
                        <Tooltip title={adCreative.name} placement="rightTop" mouseEnterDelay={1} color="#001529">
                            <Card
                                key={adCreative.id}
                                title={adCreative.name}
                                bordered={true}
                                hoverable={true}
                                style={{
                                    width: 400,
                                    height: 230,
                                    margin: 30
                                }}
                            >
                                <div>
                                    <span style={{marginRight:"10px"}}><b>ID:</b></span>
                                    <span>{adCreative.id}</span>
                                </div>
                                <div>
                                    <span style={{marginRight: "10px"}}><b>Page ID:</b></span>
                                    <span>{adCreative.object_story_spec?.page_id}</span>
                                </div>
                                <div>
                                    <span style={{marginRight: "10px"}}><b>Image Hash:</b></span>
                                    <span>{adCreative.object_story_spec?.link_data?.image_hash}</span>
                                </div>
                                <div>
                                    <span style={{marginRight: "10px"}}><b>Link:</b></span>
                                    <span>{adCreative.object_story_spec?.link_data?.link}</span>
                                </div>
                                <div>
                                    <span style={{marginRight: "10px"}}><b>Message:</b></span>
                                    <span>{adCreative.object_story_spec?.link_data?.message}</span>
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
                              width: 400,
                              height: 230,
                              margin: 30
                          }}
                    >
                        <div style={{marginTop: "70px"}}>
                            <p>Click Here to Add New AdCreative</p>
                            <FaPlus />
                        </div>
                    </Card>
                </div>
            </div>
        </div>
    );
};

export default AdCreative;
