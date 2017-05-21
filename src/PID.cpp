//    PID control:
//
// alpha = -tau_p * CTE - tau_d * d/dt CTE - tau_i * Sum(CTE)
//              P               D                  I


#include "PID.h"

//using namespace std;

PID::PID() {}

PID::~PID() {}

void PID::Init(double Kp_, double Kd_, double Ki_) {
  Kp = Kp_;
  Kd = Kd_;
  Ki = Ki_;

  p_error = 0;
  i_error = 0;
  d_error = 0;
}

void PID::UpdateError(double cte) {

  // std::cout << "1 before update: p_error = " << p_error << " / d_error = " << d_error << " / i_error = " << i_error << std::endl;

  d_error = cte - p_error;
  i_error += cte;
  p_error = cte;

  // std::cout << "2 after update: p_error = " << p_error << " / d_error = " << d_error << " / i_error = " << i_error << std::endl;

}

double PID::TotalError() {
  double alpha = -Kp * p_error - Kd * d_error - Ki * i_error;
  return alpha;
}
