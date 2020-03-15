#ifndef _VELODYNE_PLUGIN_HH_
#define _VELODYNE_PLUGIN_HH_

#include "gazebo/gazebo.hh"
#include "gazebo/physics/physics.hh"

namespace gazebo{

    class VelodynePlugin : public ModelPlugin{

        physics::ModelPtr model;
        physics::JointPtr joint;
        common::PID pid;

        public:VelodynePlugin(){}

        /// \brief The load function is called by Gazebo when the plugin is
        /// inserted into simulation
        /// \param[in] _model A pointer to the model that this plugin is
        /// attached to.
        /// \param[in] _sdf A pointer to the plugin's SDF element.
        public:virtual void Load(physics::ModelPtr _model, sdf::ElementPtr _sdf){

            std::cerr << "\nThe Velodyne plugin is attaced to model[" <<
                _model->GetName() << "]\n";

            // Safety Check
            if(_model->GetJointCount() == 0){

                std::cerr << "Invalid joint count, Velodyne plugin not loaded \n";
                return;
            }

            // Store the model pointer for convenience
            this->model = _model;

            // Get the first joint. 
            // We are making an assumption about the model having one joint that is the rotational joint
            this->joint = _model->GetJoints()[0];

            // Set up P-controller to the joint
            this->pid = common::PID(0.1, 0, 0);

            // Apply the P-controller to the joint
            this->model->GetJointController()->SetVelocityPID(
                this->joint->GetScopedName(), this->pid
            );

            // Set the joint's taret velocity. This target velocity is just for demonstration purpose.
            this->model->GetJointController()->SetVelocityTarget(
                this->joint->GetScopedName(), 10.0
            );
        }
    };

    GZ_REGISTER_MODEL_PLUGIN(VelodynePlugin);
}

#endif