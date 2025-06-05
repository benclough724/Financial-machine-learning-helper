import { useState } from 'react';
import { DataTable } from "@/components/ui/data-table";



// Defining interface for data types of rows in db
interface DatasetRows{

}


export default function DataView() {
  const [dataset, setDataset] = useState("");

  return (
    <div className="">
      <DataTable />
    </div>
  );
}
