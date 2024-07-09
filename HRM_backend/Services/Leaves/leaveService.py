# from passlib.context import CryptContext
# from jose import JWTError, jwt
# from datetime import datetime, timedelta
# from fastapi import Depends, HTTPException
# from sqlalchemy.orm import Session
# from Config.database import get_db
# from Models.leavesModel import Leaves
# from Schema.leaveSchema import LeaveCreate,LeaveUpdate
# from Models.employeeLeaveQuotaModel import EmployeeLeaveQuota

# class LeaveService:
#     @staticmethod
#     def get_all_leaves(db: Session = Depends(get_db)):
#         return db.query(Leaves).all()
    
#     @staticmethod
#     def get_all_active_leaves(db: Session = Depends(get_db)):
#         return db.query(Leaves).filter(Leaves.deleted_at == None).all()
    
#     @staticmethod
#     def get_leaves_by_id(db: Session, leaves_id: int):
#         return db.query(Leaves).filter(Leaves.id == leaves_id).first()
    
#     @staticmethod
#     def create_leaves(leave: LeaveCreate, db: Session = Depends(get_db)):
#         # Check if leave quota exists
#         leave_quota = db.query(EmployeeLeaveQuota).filter(
#             EmployeeLeaveQuota.employee_id == leave.employee_id,
#             EmployeeLeaveQuota.leave_type_id == leave.leave_type_id,
#             EmployeeLeaveQuota.deleted_at == None
#         ).first()

#         if not leave_quota:
#             raise HTTPException(status_code=404, detail="Leave quota not found for the specified employee and leave type.")

#         # Check if there are enough available days
#         if leave_quota.available < leave.days:
#             raise HTTPException(status_code=400, detail="Insufficient leave days available.")

#         # Create the leave
#         db_leave = Leaves(
#             start_date=leave.start_date,
#             end_date=leave.end_date,
#             days=leave.days,
#             leave_type_id=leave.leave_type_id,
#             user_id=leave.user_id,
#             employee_id=leave.employee_id,
#             status=leave.status,
#             created_at=leave.created_at,
#         )

#         db.add(db_leave)
#         db.commit()
#         db.refresh(db_leave)

#         # Update the leave quota
#         leave_quota.available -= leave.days
#         leave_quota.taken += leave.days

#         db.commit()
#         db.refresh(leave_quota)

#         return db_leave
#     # def create_leaves(Leave: LeaveCreate, db: Session = Depends(get_db)):
 
#     #     db_leaves = Leaves(
#     #         start_date=Leave.start_date,
#     #         end_date=Leave.end_date,
#     #         days=Leave.days,
#     #         leave_type_id=Leave.leave_type_id,
#     #         user_id=Leave.user_id,
#     #         employee_id=Leave.employee_id,
#     #         # approved_by_id=Leave.approved_by_id,
#     #         # approved_at=Leave.approved_at,
#     #         # rejected_by_id=Leave.rejected_by_id,
#     #         # rejected_at=Leave.rejected_at,
#     #         # rejected_comment=Leave.rejected_comment,
#     #         status=Leave.status,            
#     #         created_at=Leave.created_at,
#     #     )

#     #     db.add(db_leaves)
#     #     db.commit()
#     #     db.refresh(db_leaves)

#     #     return db_leaves
#     @staticmethod
#     def delete_leaves(leave_id: int, db: Session):
#         db_leaves = db.query(Leaves).filter(Leaves.id == leave_id).first()

#         if db_leaves:
#             db_leaves.soft_delete()  
#             db.commit()

#         return db_leaves
#     @staticmethod
#     def create_leaves(leave: LeaveCreate, db: Session = Depends(get_db)):
#         # Check if leave quota exists
#         leave_quota = db.query(EmployeeLeaveQuota).filter(
#             EmployeeLeaveQuota.employee_id == leave.employee_id,
#             EmployeeLeaveQuota.leave_type_id == leave.leave_type_id,
#             EmployeeLeaveQuota.deleted_at == None
#         ).first()

#         if not leave_quota:
#             raise HTTPException(status_code=404, detail="Leave quota not found for the specified employee and leave type.")

#         # Check if there are enough available days
#         if leave_quota.available < leave.days:
#             raise HTTPException(status_code=400, detail="Insufficient leave days available.")

#         # Create the leave
#         db_leave = Leaves(
#             start_date=leave.start_date,
#             end_date=leave.end_date,
#             days=leave.days,
#             leave_type_id=leave.leave_type_id,
#             user_id=leave.user_id,
#             employee_id=leave.employee_id,
#             status=leave.status,
#             created_at=leave.created_at,
#         )

#         db.add(db_leave)
#         db.commit()
#         db.refresh(db_leave)

#         # Update the leave quota
#         leave_quota.available -= leave.days
#         leave_quota.taken += leave.days

#         db.commit()
#         db.refresh(leave_quota)

#         return db_leave
    

#     @staticmethod
#     def update_leaves(leave_id: int, leaves: LeaveUpdate, db: Session = Depends(get_db)):
#         db_leave = db.query(Leaves).filter(Leaves.deleted_at == None, Leaves.id == leave_id).first()

#         if not db_leave:
#             raise HTTPException(status_code=404, detail="Leave not found")

#         if leaves.status == "Approved":
#             # Update leave details
#             if leaves.start_date is not None:
#                 db_leave.start_date = leaves.start_date
#             if leaves.end_date is not None:
#                 db_leave.end_date = leaves.end_date
#             if leaves.days is not None:
#                 db_leave.days = leaves.days
#             if leaves.leave_type_id is not None:
#                 db_leave.leave_type_id = leaves.leave_type_id
#             if leaves.employee_id is not None:
#                 db_leave.employee_id = leaves.employee_id
#             if leaves.approved_by_id is not None:
#                 db_leave.approved_by_id = leaves.approved_by_id
#             if leaves.approved_at is not None:
#                 db_leave.approved_at = leaves.approved_at
#             if leaves.status is not None:
#                 db_leave.status = leaves.status
#             if leaves.user_id is not None:
#                 db_leave.user_id = leaves.user_id
#             if leaves.updated_at is not None:
#                 db_leave.updated_at = leaves.updated_at
            
#             # Update leave quota
#             update_leave_quota(db_leave, db)

#         elif leaves.status == "Rejected":
#             # Update leave details
#             if leaves.rejected_by_id is not None:
#                 db_leave.rejected_by_id = leaves.rejected_by_id
#             if leaves.rejected_at is not None:
#                 db_leave.rejected_at = leaves.rejected_at
#             if leaves.rejected_comment is not None:
#                 db_leave.rejected_comment = leaves.rejected_comment
#             if leaves.status is not None:
#                 db_leave.status = leaves.status
#             if leaves.updated_at is not None:
#                 db_leave.updated_at = leaves.updated_at
            
#             # Revert leave quota
#             revert_leave_quota(db_leave, db)

#         db.commit()
#         db.refresh(db_leave)

#         return db_leave

# def update_leave_quota(leave: Leaves, db: Session):
#     leave_quota = db.query(EmployeeLeaveQuota).filter(
#         EmployeeLeaveQuota.employee_id == leave.employee_id,
#         EmployeeLeaveQuota.leave_type_id == leave.leave_type_id,
#         EmployeeLeaveQuota.deleted_at == None
#     ).first()

#     if not leave_quota:
#         raise HTTPException(status_code=404, detail="Leave quota not found for the specified employee and leave type.")

#     # If approved, update taken and available days
#     if leave.status == "Approved":
#         leave_quota.taken += leave.days
#         leave_quota.available -= leave.days

#     # If rejected, revert taken days
#     elif leave.status == "Rejected":
#         leave_quota.taken -= leave.days

#     db.commit()
#     db.refresh(leave_quota)

# def revert_leave_quota(leave: Leaves, db: Session):
#     leave_quota = db.query(EmployeeLeaveQuota).filter(
#         EmployeeLeaveQuota.employee_id == leave.employee_id,
#         EmployeeLeaveQuota.leave_type_id == leave.leave_type_id,
#         EmployeeLeaveQuota.deleted_at == None
#     ).first()

#     if not leave_quota:
#         raise HTTPException(status_code=404, detail="Leave quota not found for the specified employee and leave type.")

#     # Revert taken days
#     leave_quota.taken -= leave.days

#     db.commit()
#     db.refresh(leave_quota)

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from Models.leavesModel import Leaves
from Schema.leaveSchema import LeaveUpdate,LeaveCreate
from Models.employeeLeaveQuotaModel import EmployeeLeaveQuota
from Config.database import get_db

class LeaveService:
    @staticmethod
    def get_all_leaves(db: Session = Depends(get_db)):
        return db.query(Leaves).all()
    
    @staticmethod
    def get_all_active_leaves(db: Session = Depends(get_db)):
        return db.query(Leaves).filter(Leaves.deleted_at == None).all()
    
    @staticmethod
    def get_leave_by_id(db: Session, leave_id: int):
        return db.query(Leaves).filter(Leaves.id == leave_id, Leaves.deleted_at == None).first()
    
    @staticmethod
    def create_leaves(leave_data: LeaveCreate, db: Session = Depends(get_db)):
        leave_quota = db.query(EmployeeLeaveQuota).filter(
            EmployeeLeaveQuota.employee_id == leave_data.employee_id,
            EmployeeLeaveQuota.leave_type_id == leave_data.leave_type_id,
            EmployeeLeaveQuota.deleted_at == None
        ).first()

        if not leave_quota:
            raise HTTPException(status_code=404, detail="Leave quota not found for the specified employee and leave type.")

        if leave_quota.available < leave_data.days:
            raise HTTPException(status_code=400, detail="Insufficient leave days available.")

        db_leave = Leaves(
            start_date=leave_data.start_date,
            end_date=leave_data.end_date,
            days=leave_data.days,
            leave_type_id=leave_data.leave_type_id,
            user_id=leave_data.user_id,
            employee_id=leave_data.employee_id,
            status=leave_data.status,
            created_at=datetime.utcnow()  # Assuming you want to set the current timestamp
        )

        db.add(db_leave)
        db.commit()
        db.refresh(db_leave)

        # Update leave quota
        leave_quota.available -= leave_data.days
        leave_quota.taken += leave_data.days

        db.commit()
        db.refresh(leave_quota)

        return db_leave
    
    @staticmethod
    def update_leaves(leave_id: int, leave_update: LeaveUpdate, db: Session = Depends(get_db)):
        db_leave = db.query(Leaves).filter(Leaves.deleted_at == None, Leaves.id == leave_id).first()

        if not db_leave:
            raise HTTPException(status_code=404, detail="Leave not found")

        if leave_update.status == "Approved":
            # Update leave details
            db_leave.start_date = leave_update.start_date if leave_update.start_date is not None else db_leave.start_date
            db_leave.end_date = leave_update.end_date if leave_update.end_date is not None else db_leave.end_date
            db_leave.days = leave_update.days if leave_update.days is not None else db_leave.days
            db_leave.leave_type_id = leave_update.leave_type_id if leave_update.leave_type_id is not None else db_leave.leave_type_id
            db_leave.employee_id = leave_update.employee_id if leave_update.employee_id is not None else db_leave.employee_id
            db_leave.approved_by_id = leave_update.approved_by_id if leave_update.approved_by_id is not None else db_leave.approved_by_id
            db_leave.approved_at = leave_update.approved_at if leave_update.approved_at is not None else db_leave.approved_at
            db_leave.status = leave_update.status if leave_update.status is not None else db_leave.status
            db_leave.user_id = leave_update.user_id if leave_update.user_id is not None else db_leave.user_id
            db_leave.updated_at = datetime.utcnow()

            # Update leave quota
            update_leave_quota(db_leave, db)

        elif leave_update.status == "Rejected":
            # Update leave details
            db_leave.rejected_by_id = leave_update.rejected_by_id if leave_update.rejected_by_id is not None else db_leave.rejected_by_id
            db_leave.rejected_at = leave_update.rejected_at if leave_update.rejected_at is not None else db_leave.rejected_at
            db_leave.rejected_comment = leave_update.rejected_comment if leave_update.rejected_comment is not None else db_leave.rejected_comment
            db_leave.status = leave_update.status if leave_update.status is not None else db_leave.status
            db_leave.updated_at = datetime.utcnow()

            # Revert leave quota
            revert_leave_quota(db_leave, db)

        db.commit()
        db.refresh(db_leave)

        return db_leave

    @staticmethod
    def delete_leave(leave_id: int, db: Session):
        db_leave = db.query(Leaves).filter(Leaves.id == leave_id).first()

        if db_leave:
            db_leave.soft_delete()
            db.commit()

        return db_leave

def update_leave_quota(leave: Leaves, db: Session):
    leave_quota = db.query(EmployeeLeaveQuota).filter(
        EmployeeLeaveQuota.employee_id == leave.employee_id,
        EmployeeLeaveQuota.leave_type_id == leave.leave_type_id,
        EmployeeLeaveQuota.deleted_at == None
    ).first()

    if not leave_quota:
        raise HTTPException(status_code=404, detail="Leave quota not found for the specified employee and leave type.")

    # If approved, update taken and available days
    if leave.status == "Approved":
        leave_quota.taken += leave.days
        leave_quota.available -= leave.days

    db.commit()
    db.refresh(leave_quota)

def revert_leave_quota(leave: Leaves, db: Session):
    leave_quota = db.query(EmployeeLeaveQuota).filter(
        EmployeeLeaveQuota.employee_id == leave.employee_id,
        EmployeeLeaveQuota.leave_type_id == leave.leave_type_id,
        EmployeeLeaveQuota.deleted_at == None
    ).first()

    if not leave_quota:
        raise HTTPException(status_code=404, detail="Leave quota not found for the specified employee and leave type.")

    # Revert taken days
    leave_quota.taken -= leave.days

    db.commit()
    db.refresh(leave_quota)
