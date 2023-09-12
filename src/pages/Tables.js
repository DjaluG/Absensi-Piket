import {
  Row,
  Col,
  Card,
  Table,
  message,
  Button,
  Radio,
  Typography,
} from "antd";



import { ToTopOutlined } from "@ant-design/icons";
import { useState } from "react";
// import { Link } from "react-router-dom";


const { Title } = Typography;


// Define the dummy data
const fakeData = [
  {
    nis: "12345",
    name: "John Doe",
    rombel: "PPLG XII-3",
    jadwal: "Kamis",
    status: "Hadir",
    // date: "2023-08-28",
  },
  {
    nis: "5291",
    name: "Keiwa",
    rombel: "PPLG XII-3",
    jadwal: "Senin",
    status: "Hadir",
    // date: "2023-08-28",
  },
  {
    nis: "54321",
    name: "Jane Smith",
    rombel: "DKV XII-3",
    jadwal: "Senin",
    status: "Alpha",
  },{
    nis: "8129",
    name: "Wei",
    rombel: "PENG XII-3",
    jadwal: "Selasa",
    status: "Sakit",
  },
];

const daysOrder = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"];

const columns = [
  {
    title: "NIS",
    dataIndex: "nis",
    key: "nis",
  },
  {
    title: "Name",
    dataIndex: "name",
    key: "name",
  },
  {
    title: "Rombel",
    dataIndex: "rombel",
    key: "rombel",
  },
  {
    title: "Jadwal",
    dataIndex: "jadwal",
    key: "jadwal",
  },
  {
    title: "Status",
    dataIndex: "status",
    key: "status",
    render: (status) => {
      let color = "default";
      if (status === "Hadir") {
        color = "#52c41a"; // Green color
      } else if (status === "Alpha") {
        color = "#ed2b2b";
      } else if (status === "Sakit" || status === "Izin") {
        color = "#1890ff"; // Blue color
      }

      return <Button style={{ backgroundColor: color, borderColor: color, color: "#fff" }}>{status}</Button>;
    },
  },
];


function Tables() {

  const [selectedJadwal, setSelectedJadwal] = useState("Senin"); // Default to "Senin"

  const onChange = (e) => {
    const selected = e.target.value;
    setSelectedJadwal(selected);
  };

  // Filter data based on selected jadwal
  const filteredData = fakeData.filter(item => item.jadwal === selectedJadwal);
  const startDate = new Date("2023-08-21"); // Replace with your start date
  const currentDate = new Date();
  const weekDifference = Math.floor((currentDate - startDate) / (7 * 24 * 60 * 60 * 1000));

  const paginationConfig = {
    current: weekDifference + 1, // Add 1 to start pagination from 1
    pageSize: 10, // Change the pageSize if needed
  };

  return (
    <div className="tabled">
    <Row gutter={[24, 0]}>
      <Col xs="24" xl={24}>
        <Card bordered={false} className="criclebox tablespace mb-24">
          <div className="table-responsive">
             <Radio.Group onChange={onChange} value={selectedJadwal}>
                {daysOrder.map(jadwal => (
                  <Radio.Button key={jadwal} value={jadwal}>
                    {jadwal}
                  </Radio.Button>
                ))}
              </Radio.Group>
            <Table
              columns={columns.filter(col => ["nis", "name", "rombel", "jadwal", "status"].includes(col.dataIndex))}
              dataSource={filteredData}
              pagination={paginationConfig}
              className="ant-border-space"
              title={() => <Title level={4}>{`Tabel Siswa - ${selectedJadwal}`}</Title>}
            />
          </div>
        </Card>
      </Col>
    </Row>
  </div>
  );
}

export default Tables;
